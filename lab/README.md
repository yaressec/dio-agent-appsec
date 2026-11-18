# Laboratório de análise (código seu, isolado)

Esta pasta contém o código usado para validar a skill `vulnerability-analysis`.

| Arquivo | O que é |
|---------|---------|
| `app.py` | Aplicação **intencionalmente vulnerável**: login com SQL concatenado |
| `app_fixed.py` | Versão corrigida: query parametrizada e hash PBKDF2 com salt |

## Como executar

```bash
python3 lab/app.py
python3 lab/app_fixed.py
```

Os dois usam SQLite em memória. Não há servidor, rede, dados reais ou dependências externas.

## Execução responsável

- ❌ Não exponha `app.py` em produção nem em uma interface pública.
- ✅ Use-o apenas para estudar o fluxo `entrada do usuário -> query SQL`.
- ✅ A demonstração de injeção registrada em `evidence/` usa somente este arquivo local.

> O objetivo do laboratório é **entender o mecanismo e a correção**, não coletar payloads.
