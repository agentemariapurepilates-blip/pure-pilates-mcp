# Formas Permitidas — Pure Pilates

Conjunto de formas geométricas da linguagem visual da Pure (cantos arredondados + 1 canto reto, pílulas, círculo e ícones do sistema). Foram desenhadas juntas num "sheet", mas **cada forma pode ser usada isoladamente**. Sempre em Vermelho Pure `#C12030` (ou cinza escuro `#231F20` / branco) — nunca dourado.

> Notação CSS de `border-radius`: `top-left top-right bottom-right bottom-left` (TL TR BR BL).

## 1. Pétala (blob de 1 canto reto) — forma-assinatura
Quadrado/retângulo com 3 cantos totalmente arredondados + 1 canto reto. É a forma dos cards e do hero.
- **Receita email-safe (CSS, elemento ~quadrado):** `border-radius: 50% 50% 0 50%;` (canto reto embaixo-direita)
  - Rotações: embaixo-esq `50% 50% 50% 0` · cima-esq `0 50% 50% 50%` · cima-dir `50% 0 50% 50%`
  - Versão "card" (menos circular): raio fixo grande, ex. `120px 120px 0 120px`.
- **SVG (viewBox 0 0 500 500), canto reto embaixo-direita:**
  `M500 500 L250 500 C120 500 0 390 0 260 C0 120 120 0 260 0 C390 0 500 110 500 250 Z`
- Uso: cards numerados, blocos de destaque, hero.

## 2. Círculo
- `border-radius: 50%;` num elemento quadrado.
- Uso: ícone-base, número de etapa, selo, círculo de seta.

## 3. Pílula / stadium (horizontal)
- Retângulo largo, pontas 100% arredondadas: `border-radius: 999px;`
- Uso: botão/CTA, badge, divisória.

## 4. Pílula vertical
- Retângulo alto, topo e base arredondados: `border-radius: 999px;`

## 5. Meia-pílula / "D" (arredondado só de um lado)
- Ex. lado direito: `border-radius: 0 999px 999px 0;` · lado esquerdo: `999px 0 0 999px;`

## 6. Topo arredondado (arco) / hero
- Só os 2 cantos de cima: `border-radius: 999px 999px 0 0;`
- Hero do e-mail (largo, 3 cantos grandes + 1 reto embaixo-esq): `border-radius: 140px 140px 140px 0;`

## 7. Retângulo de 1 canto arredondado
- Ex.: `border-radius: 60px 0 0 0;` (suaviza só um canto). Uso: blocos, faixas.

## 8. Etiqueta / tag (%) — ícone do sistema
- Tem entalhe → não dá em `border-radius`. Usar **imagem PNG** (e-mail) ou SVG (só Apple Mail). Uso: promoções, planos de mensalidade.

## 9. Coração — ícone do sistema
- Saúde / bem-estar / amor pelo método. Usar **PNG/SVG** (border-radius não faz coração).

## Regra de renderização em e-mail
- **`border-radius`** funciona em Gmail, Apple Mail, iOS e webmails; **Outlook (Windows) ignora** e mostra cantos retos (degrada ok, continua legível).
- **SVG inline NÃO renderiza em Gmail nem Outlook** — só Apple Mail/iOS. Para formas que não dão em CSS (coração, tag, pétala muito complexa), exportar **PNG**.
- Cor sempre `#C12030` (nunca `#c10230` nem dourado). Ver [[padrao-de-email-html]].

---

---

## Refinamento — forma-assinatura em card vertical (aprendizado prático)

A forma-assinatura da Pure é **assimétrica: 3 cantos bem redondos + 1 canto reto** (canto de 90° que dá personalidade). Aprendizados ao aplicar em card de e-mail (mais alto que largo):

- **NÃO usar `50%` em célula alta:** vira "ovo" (o topo arredonda inteiro). O `50%` só funciona em elemento ~quadrado.
- **NÃO arredondar os 4 cantos iguais:** perde a essência, fica card genérico/convencional.
- **NÃO usar raio pequeno (ex: 40px) com 1 canto reto:** os outros cantos ficam quase quadrados e o canto reto parece "defeito pontudo".
- **Receita que funciona** (card ~180px largura): **raio generoso porém menor que a metade da largura** + 1 canto reto. Ex.: `border-radius: 70px 70px 0 70px` (canto reto embaixo-direita). Mantém um trecho de borda reta entre as curvas (não vira ovo) e o canto reto vira detalhe de estilo intencional.
- Variar qual canto é o reto p/ ritmo visual: `70px 70px 0 70px` (BR) · `70px 70px 70px 0` (BL) · `0 70px 70px 70px` (TL) · `70px 0 70px 70px` (TR).

Regra geral: **sempre manter 1 canto reto** nas formas-blob da Pure — é a assinatura. Renderiza no Gmail/Apple; no Outlook degrada pra retângulo (sem quebrar).
