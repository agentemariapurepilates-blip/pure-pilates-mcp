# Formas com contorno (outline) e kit de assets PNG/SVG — Pure Pilates

As formas da marca (pétala, banner+rabinho, canto único, "D", pílula, círculo) podem ser usadas **só com a linha do contorno** (fundo transparente), além da versão preenchida (cheia). Útil pra variar a peça, dar leveza, aplicar sobre foto/fundo colorido. Sempre nas cores da marca — vermelho `#C12030`, branco `#FFFFFF` ou cinza escuro `#231F20`; nunca dourado.

## Como fazer o contorno
- **Em e-mail (HTML):** trocar o preenchimento por borda — `border:3px solid #C12030; background:transparent;` mantendo o mesmo `border-radius`. O texto entra normal na célula (cor `#C12030` ou `#231F20`). Espessura: 1px = delicado, 3px = encorpado. ⚠️ Outlook desktop ignora `border-radius` → o contorno vira retângulo (degrada, não quebra).
- **Em design / Canva / impressão:** **SVG** com `fill="none" stroke="#C12030" stroke-width="5"`. Vetor = escala infinita e recolorível dentro do Canva. (SVG NÃO renderiza em e-mail — Gmail/Outlook removem; pra e-mail use a borda em CSS ou PNG.)
- **Contorno branco** (`#FFFFFF`) para usar sobre fundo escuro/vermelho.

## Kit de assets pronto (pra Canva)
4 formas × 3 versões (cheia · contorno vermelho · contorno branco), gerados no projeto:
- **PNG transparente em alta resolução (4×)** na pasta `formas-png/` — arrastar direto no Canva (menu Uploads). Recortado, sem retângulo atrás.
- **SVG vetorial** na pasta `formas-svg/` — escala infinita + recolorir no Canva.

As 4 formas-padrão e seus raios (ordem `border-radius`: sup-esq · sup-dir · inf-dir · inf-esq):
| Forma | border-radius (em ~520×200 ou ~250×250) |
|---|---|
| 1 · Banner + rabinho | `80px 140px 140px 0` |
| 2 · Canto único (sup-esq) | `160px 0 0 0` |
| 3 · Pétala (assinatura) | `50% 50% 0 50%` |
| 4 · "D" (arco só à direita) | `0 130px 130px 0` |

(Render gerado via Chrome headless com fundo transparente — `Emulation.setDefaultBackgroundColorOverride` alpha 0.)
