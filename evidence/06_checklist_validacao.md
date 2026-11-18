# Checklist de validação do projeto

Antes de publicar, conferi item por item:

- [x] `skills/vulnerability-analysis/SKILL.md` existe e tem `name` e `description` no frontmatter.
- [x] `skills/vulnerability-analysis/README.md` explica a skill para pessoas.
- [x] `agent/knowledge/security-basics.md` cobre vulnerabilidade, ameaça, risco, tríade CIA e boas práticas.
- [x] `agent/persona.md` recebeu o trecho de especialização em segurança.
- [x] `AGENTS.md` tem a skill na tabela e o novo arquivo de conhecimento na lista.
- [x] `README.md` tem a skill na tabela de skills.
- [x] `lab/app.py` é vulnerável e `lab/app_fixed.py` é seguro; ambos executam.
- [x] Teste real confirmou: injeção aceita no vulnerável, rejeitada no corrigido (`evidence/00`).
- [x] A skill perguntou contexto antes da análise (`evidence/01`).
- [x] A análise saiu em formato fixo com impacto/probabilidade/severidade (`evidence/02`).
- [x] A reanálise confirmou a mitigação e apontou riscos residuais (`evidence/03`).
- [x] O cenário Ubuntu mostrou o agente perguntando antes de sugerir comandos (`evidence/04`).
- [x] Comparação com chat genérico documentada (`evidence/05`).
- [x] Revisão da skill pelo próprio agente, com perguntas em vez de resposta pronta (`evidence/07`).
- [x] Nenhum teste foi executado contra sistema de terceiros.
- [x] Todos os arquivos citados no README existem e têm conteúdo.

## Limitação conhecida (transparência)

O Hermes não estava instalado no ambiente de validação e não havia modelo local
disponível. Por isso, os diálogos foram conduzidos pelo assistente aplicando o
`SKILL.md` linha a linha, inclusive a regra de uma pergunta por vez. Isso valida
que o **roteiro** está claro e aplicável, mas não substitui uma execução real no
Hermes. O README registra essa limitação.
