# Pure Pilates MCP

Servidor MCP que entrega os guias da Pure Pilates pra qualquer assistente de IA que suporte o protocolo MCP (Claude Desktop, Cursor, etc.).

## O que tem dentro

Três categorias, cada uma é uma ferramenta MCP:

- **`copy`** → tudo de texto e editorial (tom de voz, vocabulário, exemplos)
- **`layout`** → cores, brandbook, tipografia, logo, identidade visual
- **`ti`** → como criar SAAS, landing pages e outras práticas técnicas

Cada categoria carrega **todos** os arquivos `.md` da pasta correspondente no GitHub, concatenados. Adicionar um guia novo é só criar um `.md` na pasta certa — **não precisa mexer no código**.

## Como funciona

O servidor busca o conteúdo direto de um repositório GitHub em tempo real. Pra atualizar qualquer guia, você edita o arquivo `.md` no GitHub (pelo navegador, sem precisar de git). Em até 1 minuto, qualquer pessoa que estiver usando o MCP recebe a versão nova — sem reinstalar nada.

## Como usar (em qualquer máquina)

No cliente MCP (ex: Claude Desktop), adicione na configuração:

```json
{
  "mcpServers": {
    "pure-pilates": {
      "command": "uvx",
      "args": ["pure-pilates-mcp"]
    }
  }
}
```

Pronto. As ferramentas `copy`, `layout` e `ti` ficam disponíveis.

## Como editar os guias (sem código)

1. Abra o repositório no GitHub
2. Navegue até `content/copy/`, `content/layout/` ou `content/ti/`
3. Clique no arquivo desejado
4. Clique no ícone de lápis (canto superior direito) pra editar
5. Faça as mudanças e clique em **Commit changes**
6. Em até 1 minuto, o MCP entrega a versão atualizada

## Como adicionar um guia novo

1. Vá até a pasta da categoria (`content/copy/`, `content/layout/` ou `content/ti/`)
2. Clique em **Add file → Create new file**
3. Nome do arquivo: `nome-do-guia.md`
4. Escreva o conteúdo em Markdown
5. Commit — pronto. Aparece automaticamente na ferramenta correspondente

## Apontar pra outro repositório

Defina as variáveis de ambiente:

```
PURE_PILATES_REPO=seu_usuario/seu_repo
PURE_PILATES_BRANCH=main
```

## Estrutura do projeto

```
.
├── pyproject.toml      → config do pacote Python
├── README.md           → este arquivo
├── server.py           → o servidor MCP (1 arquivo, ~80 linhas)
└── content/            → templates dos guias (a fonte oficial fica no GitHub)
    ├── copy/
    │   ├── tom-de-voz.md
    │   ├── vocabulario.md
    │   └── exemplos.md
    ├── layout/
    │   ├── cores.md
    │   ├── tipografia.md
    │   ├── logo.md
    │   └── brandbook.md
    └── ti/
        ├── saas.md
        └── landing-pages.md
```

## Rodar localmente (pra testar)

```
uv run server.py
```

## Publicar nova versão no PyPI

```
uv build
uv publish
```
