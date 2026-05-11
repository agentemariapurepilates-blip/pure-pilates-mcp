# Tipografia — Pure Pilates

## Família tipográfica oficial

**Montserrat** — única família tipográfica permitida em todas as peças institucionais, online e offline.

- **Por que Montserrat**: visual sério, moderno, alta legibilidade, e por ser gratuita (Google Fonts) facilita adaptação em todos os materiais — site, e-mail, apresentações, peças impressas.
- **Onde baixar**: https://fonts.google.com/specimen/Montserrat
- **CSS web**: `font-family: 'Montserrat', sans-serif;`

## Hierarquia de pesos

| Hierarquia | Peso Montserrat | Uso |
|---|---|---|
| **Títulos** | Bold (700) | Headlines, H1, chamadas principais, números de destaque |
| **Subtítulos** | Medium (500) | H2/H3, texto de corpo maior, sublinhas |
| **Texto** | Light (300) ou Regular (400) | Corpo de texto, legendas, textos específicos, observações |

## Regras de aplicação

- **Cor padrão de texto**: Cinza escuro Pure `#231F20` sobre fundo claro; branco `#FFFFFF` sobre fundo escuro
- **Destaque em texto**: usar **Bold** + Vermelho Pure `#C12030`. Nunca usar itálico só pra enfatizar — usar peso
- **Alinhamento**: preferência por alinhamento à esquerda em textos longos; centralizado apenas em chamadas curtas/títulos
- **Caixa**: títulos podem ser em CAIXA ALTA quando curtos e de impacto. Textos longos sempre em caixa baixa
- **Letter-spacing**: padrão. "PILATES" no logo é a única exceção (espaçamento aumentado já embutido no logo)
- **Line-height**: 1.4 a 1.6 para corpo de texto. Títulos podem usar 1.1–1.2

## Tamanhos sugeridos (referência web/landing page)

| Elemento | Tamanho desktop | Tamanho mobile |
|---|---|---|
| H1 / Hero | 56–72 px | 36–44 px |
| H2 | 36–48 px | 28–32 px |
| H3 | 24–28 px | 20–22 px |
| Corpo de texto | 16–18 px | 16 px |
| Legenda / Small | 14 px | 13 px |
| Botão / CTA | 16–18 px Bold | 16 px Bold |

> Estes são valores de referência para LLM gerando landing pages. Ajustar conforme o design final.

## Fontes PROIBIDAS

NÃO usar em peças institucionais da Pure Pilates:

- Times New Roman, Georgia, ou qualquer serifa em textos institucionais
- Arial, Helvetica, Calibri em peças de identidade visual (apenas como fallback de e-mail)
- Comic Sans, Papyrus, fontes manuscritas ou decorativas
- Fontes condensed extremas, expanded extremas
- Mais de uma família por peça — sempre só Montserrat

## Fallback técnico (e-mail / sistemas sem Montserrat)

Em casos onde Montserrat não carrega (e-mail outlook, sistemas antigos), usar nesta ordem:

```css
font-family: 'Montserrat', 'Helvetica Neue', Helvetica, Arial, sans-serif;
```
