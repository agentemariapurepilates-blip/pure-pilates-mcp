# Modelo de E-mail HTML — Unidade ESTÚDIOS

Modelo aprovado pela Maria para e-mails marketing da unidade de negócios **estúdios**. Baseado no padrão geral (`padrao-de-email-html`) + formas da marca (`formas-permitidas`), com as decisões específicas de estúdios abaixo.

## Identidade do modelo estúdios
| Item | Valor |
|---|---|
| Fundo | **creme claro `#F6EFE2`** sólido (tint claro do laranja; é o tom dos posts de estúdio) |
| Estrutura | **SEM card branco** — conteúdo sentando direto no creme (mais imersivo) |
| Vermelho | `#C12030` (hero, cards, headings) |
| Laranja | `#DB9828` (divisória, ícone de seta) |
| Texto | `#231F20` |
| Fonte | `'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif` (Montserrat só em Apple Mail/iOS; resto Arial) |
| Hero | `border-radius:140px 140px 140px 0` (3 cantos redondos + 1 reto) |
| Cards numerados | `border-radius:70px 70px 0 70px` (3 cantos redondos + 1 reto) |

## Estrutura vertical
Hero (headline) → parágrafo intro → divisória laranja → bloco de benefício → ícone de seta ↓ → seção com 3 cards numerados (1-2-3).

## Lembrete técnico
Tudo em cor sólida + `border-radius` (renderiza em todos os clientes). Sem web font obrigatória, sem SVG inline, sem gradiente — esses não renderizam em Gmail/Outlook. Ver [[padrao-de-email-html]] e [[formas-permitidas]].

## Template (placeholders entre [ ])

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="x-apple-disable-message-reformatting">
<title>[ASSUNTO] - Pure Pilates</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;700&display=swap" rel="stylesheet">
</head>
<body style="margin:0;padding:0;background-color:#F6EFE2;font-family:'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif;-webkit-font-smoothing:antialiased;">
<div style="display:none;max-height:0;overflow:hidden;font-size:1px;line-height:1px;color:#F6EFE2;">[PREHEADER]</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#F6EFE2;">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;">

<tr><td style="padding:0 16px 16px 16px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#C12030;border-top-left-radius:140px;border-top-right-radius:140px;border-bottom-right-radius:140px;border-bottom-left-radius:0;overflow:hidden;">
<tr><td align="center" style="padding:60px 32px 56px 32px;">
<h1 style="margin:0;font-size:32px;line-height:1.2;color:#ffffff;font-weight:bold;text-align:center;font-family:'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif;">[HEADLINE]</h1>
</td></tr></table>
</td></tr>

<tr><td align="center" style="padding:16px 40px 24px 40px;">
<p style="margin:0;font-size:14px;line-height:1.6;color:#231F20;text-align:center;font-family:'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif;">[INTRO]</p>
</td></tr>

<tr><td style="padding:0 40px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#DB9828;height:3px;border-radius:2px;"><tr><td></td></tr></table></td></tr>

<tr><td align="center" style="padding:32px 48px 16px 48px;">
<p style="margin:0;font-size:14px;line-height:1.6;color:#231F20;text-align:center;font-family:'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif;">[BENEFÍCIO]</p>
</td></tr>
<tr><td align="center" style="padding:16px 0 24px 0;"><div style="width:40px;height:40px;background-color:#DB9828;border-radius:50%;text-align:center;line-height:40px;color:#ffffff;font-size:18px;">&#8595;</div></td></tr>

<tr><td style="padding:0 24px 24px 24px;">
<h2 style="margin:0 0 20px 0;font-size:22px;color:#C12030;font-weight:bold;text-align:left;font-family:'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif;">[TÍTULO SEÇÃO]</h2>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td width="33.33%" valign="top" style="padding:0 6px 0 0;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#C12030;border-radius:70px 70px 0 70px;height:270px;">
<tr><td valign="middle" align="center" style="padding:32px 22px;height:270px;"><p style="margin:0 0 8px 0;font-size:28px;line-height:1;color:#ffffff;font-weight:bold;font-family:'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif;">1</p><p style="margin:0;font-size:12px;line-height:1.4;color:#ffffff;text-align:center;font-family:'Montserrat',Arial,'Helvetica Neue',Helvetica,sans-serif;">[PASSO 1]</p></td></tr>
</table></td>
<!-- repetir cards 2 (padding:0 3px) e 3 (padding:0 0 0 6px) -->
</tr></table>
</td></tr>

</table></td></tr></table>
</body></html>
```
