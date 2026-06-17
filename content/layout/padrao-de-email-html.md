# Padrão de E-mail HTML — Pure Pilates

Estrutura-base aprovada pela Maria para e-mails marketing em HTML. Layout validado e já alinhado ao guia oficial (cores, tipografia, formas). Use este documento como ponto de partida para qualquer novo e-mail.

## Design tokens

| Token | Valor | Uso |
|---|---|---|
| Vermelho Pure | `#C12030` | Hero, headings (H2), cards de passo, CTAs. Cor dominante. |
| Laranja (secundária) | `#DB9828` | Divisória fina, ícone/círculo de seta. Único acento secundário permitido aqui (substitui dourado, que é PROIBIDO). |
| Cinza escuro Pure | `#231F20` | Corpo de texto sobre fundo claro. |
| Branco | `#FFFFFF` | Fundo do card principal e textos sobre fundo vermelho. |
| Fundo da página (canvas) | `#f4f4f4` | Cinza-claro neutro atrás do card. Evita tom creme/"spa pastel". |
| Fonte | `'Montserrat','Helvetica Neue',Helvetica,Arial,sans-serif` | Montserrat oficial + fallback de e-mail. Incluir `<link>` Google Fonts no `<head>`. |

## Regras de construção (compatibilidade de e-mail)

- Layout 100% em `<table role="presentation">` com `cellpadding/cellspacing/border="0"` e **estilos inline** (Gmail/Outlook não leem `<style>` externo de forma confiável).
- Card central com `max-width:600px; width:100%`, `border-radius:16px`, `box-shadow` suave.
- Repetir `font-family` nos elementos de texto (`h1`,`h2`,`p`) — o Outlook não herda do `<body>`.
- Preheader oculto no topo (`display:none;max-height:0;...`) com a mesma cor do fundo (`#f4f4f4`).
- Incluir conditional MSO e `x-apple-disable-message-reformatting` no `<head>`.

## Linguagem visual (assinatura do padrão)

- **Formas "blob" arredondadas assimétricas**: 3 cantos arredondados + 1 canto reto.
  - Hero: `border-radius: 140px 140px 140px 0` (canto inferior-esquerdo reto).
  - Cards de passo: `border-radius: 120px 120px 0 120px` (canto inferior-direito reto).
- Estrutura vertical: **Hero (headline) → parágrafo intro → divisória laranja → bloco de benefício → ícone de seta → seção "Como indicar?" com 3 cards numerados (1-2-3)**.
- Headline centralizada e curta (Montserrat Bold, branco sobre vermelho). H2 de seção alinhado à esquerda em vermelho `#C12030`.

## Cuidados de copy/marca

- Tom acolhedor, aspiracional, sem promessa de "resultado rápido".
- Nome oficial do programa de indicação: **"Indique Pilates"** (pilar editorial "Você Traz, Você Ganha"). Headlines criativas como "Indique um amigo" são aceitáveis, mas o programa em si chama-se Indique Pilates.
- Um CTA principal por e-mail.

## Template base (HTML)

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="x-apple-disable-message-reformatting">
<title>Assunto - Pure Pilates</title>
<!--[if mso]>
<noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
<![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;700&display=swap');
  body { margin:0; padding:0; }
</style>
</head>
<body style="margin:0;padding:0;background-color:#f4f4f4;font-family:'Montserrat','Helvetica Neue',Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;">
<div style="display:none;max-height:0;overflow:hidden;font-size:1px;line-height:1px;color:#f4f4f4;">[PREHEADER — resumo de uma linha]</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f4f4f4;">
<tr><td align="center" style="padding:24px 12px;">

<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;background-color:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.06);">

<!-- HERO (blob: 140px 140px 140px 0) -->
<tr><td style="padding:0 16px 16px 16px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#C12030;border-top-left-radius:140px;border-top-right-radius:140px;border-bottom-right-radius:140px;border-bottom-left-radius:0;overflow:hidden;">
<tr><td align="center" style="padding:60px 32px 56px 32px;color:#ffffff;">
<h1 style="margin:0;font-size:32px;line-height:1.2;color:#ffffff;font-weight:bold;text-align:center;font-family:'Montserrat','Helvetica Neue',Helvetica,Arial,sans-serif;">[Headline]</h1>
</td></tr>
</table>
</td></tr>

<!-- INTRO -->
<tr><td align="center" style="padding:16px 40px 24px 40px;">
<p style="margin:0;font-size:14px;line-height:1.6;color:#231F20;text-align:center;font-family:'Montserrat','Helvetica Neue',Helvetica,Arial,sans-serif;">[Parágrafo intro]</p>
</td></tr>

<!-- DIVISÓRIA LARANJA -->
<tr><td style="padding:0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#DB9828;height:3px;border-radius:2px;"><tr><td></td></tr></table></td></tr>

<!-- BLOCO DE BENEFÍCIO + SETA -->
<tr><td align="center" style="padding:32px 48px 16px 48px;">
<p style="margin:0;font-size:14px;line-height:1.6;color:#231F20;text-align:center;font-family:'Montserrat','Helvetica Neue',Helvetica,Arial,sans-serif;">[Texto de benefício]</p>
</td></tr>
<tr><td align="center" style="padding:16px 0 24px 0;"><div style="width:40px;height:40px;background-color:#DB9828;border-radius:50%;text-align:center;line-height:40px;color:#ffffff;font-size:18px;">&#8595;</div></td></tr>

<!-- SEÇÃO COM CARDS NUMERADOS (blob: 120px 120px 0 120px) -->
<tr><td style="padding:0 24px 24px 24px;">
<h2 style="margin:0 0 20px 0;font-size:22px;color:#C12030;font-weight:bold;text-align:left;font-family:'Montserrat','Helvetica Neue',Helvetica,Arial,sans-serif;">[Título da seção]</h2>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td width="33.33%" valign="top" style="padding:0 6px 0 0;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#C12030;border-top-left-radius:120px;border-top-right-radius:120px;border-bottom-left-radius:120px;border-bottom-right-radius:0;height:270px;">
<tr><td valign="middle" align="center" style="padding:32px 22px;height:270px;"><p style="margin:0 0 8px 0;font-size:28px;line-height:1;color:#ffffff;font-weight:bold;font-family:'Montserrat','Helvetica Neue',Helvetica,Arial,sans-serif;">1</p><p style="margin:0;font-size:12px;line-height:1.4;color:#ffffff;text-align:center;font-family:'Montserrat','Helvetica Neue',Helvetica,Arial,sans-serif;">[Passo 1]</p></td></tr>
</table></td>
<!-- repetir cards 2 e 3 com padding:0 3px (meio) e padding:0 0 0 6px (direita) -->
</tr></table>
</td></tr>

</table></td></tr></table>
</body></html>
```

---

---

## Atualização — Fonte oficial do e-mail (decisão da Maria)

Montserrat é **web font** e NÃO renderiza em **Gmail** nem **Outlook (Windows)** — só em Apple Mail/iOS. Em e-mail, a base tem que ser uma fonte **web-safe**; o Montserrat fica apenas como *progressive enhancement*.

**Stack oficial do e-mail:**
```
font-family:'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif;
```

Regras:
- Aplicar esse stack no `<body>` **E** em cada elemento de texto (`h1`, `h2`, `p`). O Outlook não herda a fonte do `<body>` e cai em **Times New Roman** (serifada) se não for forçado `sans-serif`.
- Manter o `<link>` do Google Fonts (Montserrat) no `<head>`: Apple Mail/iOS renderizam Montserrat de verdade; os demais clientes usam Arial.
- Fontes web-safe seguras (caso precise variar): **Arial, Helvetica, Verdana, Tahoma, Trebuchet MS** (sans-serif) · **Georgia, Times New Roman** (serifadas).
- Lembrete: o Gmail só suporta nativamente as web fonts **Open Sans** e **Roboto** — nenhuma outra (incluindo Montserrat) carrega lá.

---

---

## Formas permitidas nos cards/blocos (variações)

As formas da linguagem Pure (catálogo completo no guia **`formas-permitidas`**) podem ser usadas nos blocos do e-mail — cada uma isolada.

**Card "pétala" (variação dos cards 1-2-3):** mesma forma do card padrão, porém mais arredondada (quase circular com 1 canto reto).
- Em e-mail, **preferir CSS a SVG**: `border-radius: 50% 50% 0 50%` num `<td>`/`<div>` aproximadamente quadrado — renderiza no Gmail/Apple/webmail. **SVG inline some no Gmail e no Outlook** (só Apple Mail/iOS renderiza).
- Manter a célula ~quadrada pro arredondamento ficar circular; com raio fixo grande (`120px 120px 0 120px`) fica em formato de card.
- Se usar SVG mesmo assim (ok só pra Apple Mail/iOS), trocar `fill="#c10230"` por `#C12030` e a fonte por `Arial`.

Recomendação geral: blocos/cards via **tabela + border-radius** (não SVG), pra garantir renderização no Gmail e Outlook. Formas sem solução em CSS (coração, etiqueta %) entram como **PNG**.

---

---

## Atualização (jun/2026) — aprendizados de renderização validados no Gmail real

1. **Fundos coloridos: usar `bgcolor` ALÉM do CSS.** O Gmail REMOVE `background-color` do CSS inline ao entregar — qualquer bloco colorido (hero, cards, faixas, círculo de seta) fica transparente e "some", deixando só o texto. Solução: atributo HTML `bgcolor="#C12030"` na `<table>` E no `<td>`, mantendo o `background-color` no CSS como reforço. `<div>` não aceita `bgcolor` → converter a forma em `<table>`/`<td>` (foi assim que o círculo da seta foi refeito).

2. **Hero "ponta a ponta" (full-bleed).** Para o hero encostar nas bordas dos 600px, tirar o padding lateral do wrapper (`padding:0 0 16px 0`). A forma usada é o banner com rabinho: `border-radius:80px 140px 140px 0` (3 cantos arredondados + canto inferior-esquerdo reto, com arco forte à direita).

3. **Cards "Como indicar?" — no mobile, NÃO usar 3 pétalas lado a lado.** Em colunas estreitas + texto longo, a pétala `50%` estica e vira "ovo". Solução aprovada pela Maria: **lista vertical** — cada passo numa linha, com **selo pétala 56×56** (`border-radius:50% 50% 0 50%`, número branco 24px bold) à esquerda + texto **13px** ao lado, e **linha laranja 1px** (`bgcolor="#DB9828"`) entre os passos. A pétala só fica redonda em elemento ~quadrado (o selo); nunca em card alto.

4. **Preview/teste:** o editor de RASCUNHO do Gmail "achata" o layout (tira formas/cores). Avaliar sempre pelo e-mail **RECEBIDO** na caixa de entrada, não pelo rascunho aberto. Enviar teste pra si mesmo antes de aprovar.
