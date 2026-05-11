"""MCP server da Pure Pilates — lê os guias do GitHub e permite salvar aprendizados."""

import base64
import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.request

from mcp.server.fastmcp import FastMCP

DEFAULT_REPO = "agentemariapurepilates-blip/pure-pilates-mcp"
DEFAULT_BRANCH = "main"
GITHUB_ACCOUNT = "agentemariapurepilates-blip"

REPO = os.environ.get("PURE_PILATES_REPO", DEFAULT_REPO)
BRANCH = os.environ.get("PURE_PILATES_BRANCH", DEFAULT_BRANCH)

API_BASE = f"https://api.github.com/repos/{REPO}/contents"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

CACHE_TTL_SECONDS = 60
_cache: dict[str, tuple[float, str]] = {}

NOT_LOGGED_IN_MSG = (
    "Não consegui pegar credenciais do GitHub pra escrever no MCP da Pure.\n"
    f"Verifique se você está logado na conta {GITHUB_ACCOUNT} via gh CLI:\n"
    "  1. Instale o gh CLI se não tiver: brew install gh\n"
    f"  2. Faça login com a conta da Maria: gh auth login\n"
    f"  3. Confirme que aparece em: gh auth status"
)


def _fetch(url: str) -> str | None:
    now = time.time()
    cached = _cache.get(url)
    if cached and now - cached[0] < CACHE_TTL_SECONDS:
        return cached[1]

    request = urllib.request.Request(url, headers={"User-Agent": "pure-pilates-mcp"})
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            content = response.read().decode("utf-8")
    except (urllib.error.HTTPError, urllib.error.URLError):
        return None

    _cache[url] = (now, content)
    return content


def fetch_category(category: str) -> str:
    index_url = f"{API_BASE}/content/{category}?ref={BRANCH}"
    index_raw = _fetch(index_url)
    if index_raw is None:
        return (
            f"Não consegui listar os arquivos de '{category}'.\n"
            f"Confirme que existe a pasta content/{category}/ em https://github.com/{REPO}"
        )

    try:
        files = json.loads(index_raw)
    except json.JSONDecodeError:
        return f"Erro ao decodificar a listagem de '{category}'."

    md_files = sorted(
        (f for f in files if f.get("name", "").endswith(".md")),
        key=lambda f: f["name"],
    )
    if not md_files:
        return f"Nenhum arquivo .md em content/{category}/ no repositório {REPO}."

    sections: list[str] = []
    for file_info in md_files:
        name = file_info["name"]
        raw_url = f"{RAW_BASE}/content/{category}/{name}"
        content = _fetch(raw_url)
        if content is None:
            sections.append(f"## {name}\n\n_(erro ao carregar)_")
        else:
            sections.append(content)

    return "\n\n---\n\n".join(sections)


def _get_github_token() -> str | None:
    try:
        result = subprocess.run(
            ["gh", "auth", "token", "--user", GITHUB_ACCOUNT],
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    token = result.stdout.strip()
    return token or None


def _slugify(text: str) -> str:
    text = text.lower().strip()
    replacements = {
        "á": "a", "à": "a", "â": "a", "ã": "a", "ä": "a",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "í": "i", "ì": "i", "î": "i", "ï": "i",
        "ó": "o", "ò": "o", "ô": "o", "õ": "o", "ö": "o",
        "ú": "u", "ù": "u", "û": "u", "ü": "u",
        "ç": "c", "ñ": "n",
    }
    for orig, sub in replacements.items():
        text = text.replace(orig, sub)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "sem-titulo"


def _save_to_github(category: str, titulo: str, conteudo: str) -> str:
    token = _get_github_token()
    if not token:
        return NOT_LOGGED_IN_MSG

    slug = _slugify(titulo)
    filename = f"{slug}.md"
    path = f"content/{category}/{filename}"

    check_url = f"{API_BASE}/{path}?ref={BRANCH}"
    check_request = urllib.request.Request(
        check_url,
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "pure-pilates-mcp",
            "Accept": "application/vnd.github+json",
        },
    )
    sha: str | None = None
    existing_content = ""
    try:
        with urllib.request.urlopen(check_request, timeout=10) as response:
            data = json.loads(response.read())
            sha = data.get("sha")
            if data.get("content"):
                try:
                    existing_content = base64.b64decode(data["content"]).decode("utf-8")
                except Exception:
                    existing_content = ""
    except urllib.error.HTTPError as e:
        if e.code != 404:
            return f"Erro ao verificar arquivo existente: HTTP {e.code}"
    except urllib.error.URLError as e:
        return f"Erro de conexão ao GitHub: {e}"

    if existing_content:
        new_body = f"{existing_content.rstrip()}\n\n---\n\n{conteudo.strip()}\n"
        commit_message = f"update({category}): {titulo}"
    else:
        if not conteudo.lstrip().startswith("#"):
            new_body = f"# {titulo}\n\n{conteudo.strip()}\n"
        else:
            new_body = conteudo.strip() + "\n"
        commit_message = f"add({category}): {titulo}"

    encoded = base64.b64encode(new_body.encode("utf-8")).decode("ascii")

    put_payload: dict[str, str] = {
        "message": commit_message,
        "content": encoded,
        "branch": BRANCH,
    }
    if sha:
        put_payload["sha"] = sha

    put_url = f"{API_BASE}/{path}"
    put_request = urllib.request.Request(
        put_url,
        method="PUT",
        data=json.dumps(put_payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "pure-pilates-mcp",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(put_request, timeout=15) as response:
            result = json.loads(response.read())
            commit_sha = result.get("commit", {}).get("sha", "")[:7] or "?"
            action = "Atualizado" if sha else "Criado"
            return (
                f"{action}: content/{category}/{filename} "
                f"(commit {commit_sha}). Em até 60s qualquer Claude consultando "
                f"'{category}' já vê o conteúdo novo."
            )
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        return f"Erro ao salvar no GitHub: HTTP {e.code} - {error_body[:200]}"
    except urllib.error.URLError as e:
        return f"Erro de conexão ao salvar: {e}"


mcp = FastMCP("pure-pilates")


@mcp.tool()
def copy() -> str:
    """Guias de Copy da Pure Pilates: textos, editorial, tom de voz, vocabulário e exemplos."""
    return fetch_category("copy")


@mcp.tool()
def layout() -> str:
    """Guias de Layout da Pure Pilates: cores, brandbook, tipografia, logo e identidade visual."""
    return fetch_category("layout")


@mcp.tool()
def ti() -> str:
    """Guias de TI da Pure Pilates: como criar SAAS, landing pages e outras práticas técnicas."""
    return fetch_category("ti")


@mcp.tool()
def salvar_copy(titulo: str, conteudo: str) -> str:
    """Salva um aprendizado novo no guia de Copy da Pure Pilates.
    O título vira o nome do arquivo (ex: 'tom-de-voz-em-instagram.md').
    Se já existir um arquivo com o mesmo título, adiciona o conteúdo ao final.
    Requer estar logado na conta da Maria via gh CLI."""
    return _save_to_github("copy", titulo, conteudo)


@mcp.tool()
def salvar_layout(titulo: str, conteudo: str) -> str:
    """Salva um aprendizado novo no guia de Layout da Pure Pilates.
    O título vira o nome do arquivo (ex: 'paleta-de-cores-secundaria.md').
    Se já existir um arquivo com o mesmo título, adiciona o conteúdo ao final.
    Requer estar logado na conta da Maria via gh CLI."""
    return _save_to_github("layout", titulo, conteudo)


@mcp.tool()
def salvar_ti(titulo: str, conteudo: str) -> str:
    """Salva um aprendizado novo no guia de TI da Pure Pilates.
    O título vira o nome do arquivo (ex: 'cache-de-assets-em-landing.md').
    Se já existir um arquivo com o mesmo título, adiciona o conteúdo ao final.
    Requer estar logado na conta da Maria via gh CLI."""
    return _save_to_github("ti", titulo, conteudo)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
