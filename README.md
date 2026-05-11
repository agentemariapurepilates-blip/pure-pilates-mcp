# MCP da Pure Pilates

Servidor MCP que entrega os guias da Pure Pilates (copy, layout, TI) pra qualquer assistente de IA — Claude Desktop, Claude Code, Cursor, etc. Também permite **salvar aprendizados novos** direto pelo chat, sem precisar abrir o GitHub.

## O que tem dentro

Três categorias, cada uma com tools de **ler** e **salvar**:

| Categoria | Tool de leitura | Tool de escrita | Pasta no GitHub |
|---|---|---|---|
| Copy | `copy` | `salvar_copy` | `content/copy/` |
| Layout | `layout` | `salvar_layout` | `content/layout/` |
| TI | `ti` | `salvar_ti` | `content/ti/` |

Tudo é arquivo `.md` no GitHub. O MCP busca em tempo real (cache de 60s).

---

## Como instalar (em qualquer máquina do time)

### Pré-requisitos

1. **Claude Desktop** instalado (https://claude.ai/download)
2. **uv** (ferramenta que roda o MCP)
3. **gh CLI** (apenas se você for **salvar** aprendizados; não precisa só pra ler)

### Passo 1 — Instalar o `uv`

**Mac/Linux** (no Terminal):
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows** (no PowerShell):
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Passo 2 — Conectar o MCP no Claude Desktop

Abrir o arquivo de config do Claude Desktop:

- **Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Se o arquivo não existir, cria com este conteúdo. Se já existir com outros MCPs, adiciona o bloco `pure-pilates` dentro do `mcpServers`:

```json
{
  "mcpServers": {
    "pure-pilates": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/agentemariapurepilates-blip/pure-pilates-mcp",
        "pure-pilates-mcp"
      ]
    }
  }
}
```

### Passo 3 — Reiniciar o Claude Desktop

Cmd+Q (Mac) ou fechar pelo ícone (Windows). Abrir de novo. Pronto — as tools `copy`, `layout` e `ti` já podem ser usadas.

---

## Pra salvar aprendizados (setup extra)

Pra usar as tools `salvar_copy`, `salvar_layout`, `salvar_ti`, você precisa estar logado na conta GitHub da Maria. Setup só uma vez por máquina:

### Instalar o `gh` CLI

**Mac:**
```
brew install gh
```

**Windows/Linux:** ver https://cli.github.com/

### Logar na conta da Maria

```
gh auth login
```

Escolhe na tela:
- **GitHub.com**
- **HTTPS**
- **Login with a web browser** (vai abrir o navegador — entra na conta `agentemariapurepilates-blip`)

Pra confirmar:
```
gh auth status
```

Tem que aparecer `Logged in to github.com account agentemariapurepilates-blip`.

> 💡 Quem trabalha em outros projetos da Pure provavelmente já fez isso. Pode pular esses passos.

---

## Como usar (em qualquer Claude)

### Ler os guias

> *"Me traz o guia de copy da Pure Pilates"*
>
> *"Quais são as cores da identidade visual da Pure?"*
>
> *"Como criar uma landing page da Pure?"*

### Salvar aprendizados

> *"Salva esse aprendizado no MCP da Pure, categoria TI: cache agressivo de assets versionados quebra o deploy quando..."*
>
> *"Adiciona no guia de copy da Pure: ao falar de aulas em casa, sempre usar 'pilates em casa' e nunca 'pilates remoto'"*
>
> *"Salva no layout: a paleta secundária da Pure inclui..."*

O Claude vai chamar a tool certa, criar (ou atualizar) o arquivo `.md` no GitHub, e fazer commit como Maria. Em até 60s qualquer outra pessoa do time já vê o conteúdo novo.

---

## Como editar guias diretamente no GitHub (sem código)

Alternativa pra quando você não está no Claude:

1. Abre https://github.com/agentemariapurepilates-blip/pure-pilates-mcp
2. Navega até `content/copy/`, `content/layout/` ou `content/ti/`
3. Clica no arquivo desejado → ícone de lápis → edita → **Commit changes**

Funciona do celular também.

---

## Estrutura do projeto

```
.
├── pyproject.toml      → config do pacote Python
├── README.md           → este arquivo
├── server.py           → o servidor MCP
└── content/            → guias da Pure (fonte oficial)
    ├── copy/           → textos, editorial, tom de voz
    ├── layout/         → cores, brandbook, tipografia
    └── ti/             → como criar SAAS, landing pages
```

## Configurar pra apontar pra outro repositório

```
PURE_PILATES_REPO=seu_usuario/seu_repo
PURE_PILATES_BRANCH=main
```

## Rodar localmente (pra desenvolvimento)

```
uv run server.py
```
