# Como criar um SAAS — Pure Pilates

Guia interno para qualquer projeto de software-as-a-service da Pure.

## Princípios

1. **Resolve um problema real da Pure ou da praticante.** Não criamos por hype.
2. **MVP primeiro.** Um fluxo completo (mesmo simples) vale mais que dez recursos pela metade.
3. **Métrica antes de feature.** Sabemos o que estamos medindo antes de escrever a primeira linha.

## Stack padrão recomendada

- **Front-end:** Next.js + TypeScript + Tailwind
- **Back-end:** Next.js API routes ou Python (FastAPI), conforme o caso
- **Banco:** PostgreSQL (Supabase para começar — auth e DB juntos)
- **Auth:** Supabase Auth ou Clerk
- **Pagamento:** Stripe
- **Deploy:** Vercel (front) + Supabase (DB)
- **Monitoramento:** Sentry para erros, PostHog para produto

## Fluxo de criação

1. **Descobrir** — escrever em 1 página: problema, persona, hipótese de solução, métrica de sucesso
2. **Validar** — testar com 5 pessoas da persona antes de codificar
3. **Construir MVP** — escopo mínimo, prazo máximo de 6 semanas
4. **Lançar pra 10 usuárias-piloto** — feedback semanal
5. **Iterar ou matar** — se não bater a métrica de sucesso em 60 dias, mata

## Padrões de código

- Sempre TypeScript no front (zero `any`)
- Funções puras quando possível
- Variáveis de ambiente em `.env.local` (nunca commit)
- Commits em português, no presente: "adiciona", "corrige", "remove"

## Segurança mínima

- Senhas nunca em texto puro (hash com bcrypt/argon2 — Supabase já faz)
- HTTPS obrigatório em produção
- Validar inputs no servidor, sempre
- LGPD: coletar só o necessário, deixar exclusão de conta acessível
