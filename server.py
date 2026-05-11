"""MCP server da Pure Pilates — busca os guias direto do GitHub."""

import json
import os
import time
import urllib.error
import urllib.request

from mcp.server.fastmcp import FastMCP

DEFAULT_REPO = "agentemariapurepilates-blip/pure-pilates-mcp"
DEFAULT_BRANCH = "main"

REPO = os.environ.get("PURE_PILATES_REPO", DEFAULT_REPO)
BRANCH = os.environ.get("PURE_PILATES_BRANCH", DEFAULT_BRANCH)

API_BASE = f"https://api.github.com/repos/{REPO}/contents"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

CACHE_TTL_SECONDS = 60
_cache: dict[str, tuple[float, str]] = {}


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


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
