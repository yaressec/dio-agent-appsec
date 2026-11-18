# 🤖 DIO Agent — Especialização em Análise de Vulnerabilidades

> Este repositório é uma **evolução do [DIO Agent](https://github.com/digitalinnovationone/dio-agent)**. Ele transforma o mentor em um especialista em AppSec que pergunta o contexto antes de agir, avalia impacto/probabilidade/severidade e orienta a correção. Nenhum modelo foi treinado: o agente aprende porque os arquivos foram escritos.

---

## 🛡️ A especialização que dei ao agente (e por quê)

O DIO Agent original é um mentor de estudos. Acrescentei a ele uma postura de **AppSec mentor**:

- antes de analisar qualquer código, o agente confirma **ambiente, escopo e autorização**;
- separa **vulnerabilidade**, **ameaça** e **risco**;
- mostra o fluxo **source → sink**;
- sempre preenche **impacto, probabilidade e severidade** no mesmo formato;
- explica o mecanismo antes da correção e pede uma **nova verificação**.

**Por que essa especialização?** Porque a diferença entre um chat que "solta um payload" e um profissional de segurança está justamente no raciocínio de contexto e risco. O estudante precisa aprender a decidir prioridade, não apenas a copiar um comando. A skill é um roteiro defensivo, sem respostas prontas — alinhado com a filosofia original do DIO Agent.

> ⚠️ Todo o teste foi feito em código próprio, em laboratório isolado, sem alvos de terceiros.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| **[Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md)** | Analisa código/config/infra com foco em segurança: contexto, impacto, probabilidade, severidade e correção | "Olha esse app.py, tem um login esquisito — me ajuda como um AppSec" |

A skill nova também tem um [README para pessoas](skills/vulnerability-analysis/README.md).

---

## 📝 Arquivos criados ou alterados

| Arquivo | Ação | Conteúdo |
|---------|------|----------|
| `skills/vulnerability-analysis/SKILL.md` | **criado** | Roteiro com `name` + `description`, Regra 0 de autorização, 8 etapas e formato fixo de saída |
| `skills/vulnerability-analysis/README.md` | **criado** | Explicação da skill para leitores humanos |
| `agent/knowledge/security-basics.md` | **criado** | Vulnerabilidade, ameaça, risco, tríade CIA, CWE/CVE/CVSS, ATT&CK, boas práticas |
| `agent/persona.md` | **alterado** | Nova seção "Especialização em segurança (AppSec)" + valor de responsabilidade |
| `AGENTS.md` | **alterado** | Novo arquivo de conhecimento, linha na tabela de skills e regras 10/11 + limite de autorização |
| `README.md` | **alterado** | Linha da skill na tabela e esta seção de especialização |
| `lab/app.py`, `lab/app_fixed.py` | **criados** | Laboratório vulnerável e corrigido para os testes |
| `evidence/*` | **criados** | Diálogos, análise, reanálise, cenário Ubuntu e checklist |

---

## ▶️ Como rodar o agente no harness

1. Instale um harness (ex.: **Hermes** — documentação: https://hermes-agent.nousresearch.com/docs).
2. Baixe este repositório:
   ```bash
   git clone https://github.com/yaressec/dio-agent-appsec.git
   cd dio-agent-appsec
   ```
3. ⚠️ **Abra o terminal dentro da pasta do projeto** (a que tem `AGENTS.md`). Se você abrir o harness em outra pasta, ele não encontra os arquivos da skill — esse é o erro mais comum.
4. Converse naturalmente. Para disparar a skill:
   ```
   Como especialista em AppSec, analise o lab/app.py.
   Encontre a falha, explique o impacto e me oriente a corrigir.
   ```
5. Para validar a correção:
   ```
   Apliquei a correção em lab/app_fixed.py. Faça uma nova varredura e confirme se mitigou.
   ```

### Roteiro de teste usado

```bash
python3 lab/app.py         # login legítimo e comportamento vulnerável
python3 lab/app_fixed.py   # versão corrigida
```

`app.py` e `app_fixed.py` usam SQLite em memória, sem rede e sem dados reais.

---

## 🔬 Validação e evidências

| Evidência | O que mostra |
|-----------|--------------|
| [`evidence/00_teste_comportamento.txt`](evidence/00_teste_comportamento.txt) | Execução real: injeção aceita no app vulnerável e rejeitada no corrigido |
| [`evidence/01_contexto_antes_da_analise.txt`](evidence/01_contexto_antes_da_analise.txt) | O agente pergunta ambiente e dados **antes** de analisar |
| [`evidence/02_analise_app_vulneravel.txt`](evidence/02_analise_app_vulneravel.txt) | Análise completa: CWE-89, MITRE ATT&CK T1190, impacto/probabilidade/severidade |
| [`evidence/03_reanalise_app_corrigido.txt`](evidence/03_reanalise_app_corrigido.txt) | Confirmação da mitigação + riscos residuais (rate limiting, enumeração por tempo) |
| [`evidence/04_cenario_ubuntu_contexto.txt`](evidence/04_cenario_ubuntu_contexto.txt) | Cenário de servidor Ubuntu: contexto antes de qualquer comando |
| [`evidence/05_comparativo_chat_generico.txt`](evidence/05_comparativo_chat_generico.txt) | Chat genérico × agente especializado |
| [`evidence/06_checklist_validacao.md`](evidence/06_checklist_validacao.md) | Checklist item a item |
| [`evidence/07_revisao_da_skill.md`](evidence/07_revisao_da_skill.md) | O próprio agente revisa o SKILL.md com perguntas, sem resposta pronta |

### Prints

| # | Imagem | Cena |
|---|--------|------|
| 1 | ![Contexto](images/01_contexto.png) | Perguntas antes da análise |
| 2 | ![Análise](images/02_analise.png) | Impacto, probabilidade e severidade |
| 3 | ![Reanálise](images/03_reanalise.png) | Confirmação da mitigação |
| 4 | ![Ubuntu](images/04_ubuntu.png) | Cenário de infraestrutura |

### Melhoria escolhida

Além da skill pedida, escolhi como melhoria o **formato fixo de análise** (impacto, probabilidade e severidade sempre iguais) + a **Regra 0 de autorização**. Isso permite comparar casos diferentes e evita que o agente sugira comandos antes de saber se o ambiente é seu. Também incluí o cenário de infraestrutura (Ubuntu exposto) para testar a skill fora do código.

### Limitação conhecida (transparência)

O **Hermes não estava instalado** no ambiente de validação e não havia modelo local disponível. Os diálogos foram conduzidos pelo assistente aplicando o `SKILL.md` linha a linha, inclusive a regra de uma pergunta por vez. Isso valida que o roteiro está claro e aplicável, mas **não substitui uma execução real no Hermes**. Se você rodar no harness, os arquivos estão prontos para isso.

---

## 🗂️ Estrutura do repositório

```text
dio-agent-appsec/
├── README.md                                  # este guia
├── AGENTS.md                                  # definição do agente (alterada)
├── CLAUDE.md
├── agent/
│   ├── persona.md                             # alterada
│   └── knowledge/
│       ├── dio-platform.md
│       ├── learning-experiences.md
│       └── security-basics.md                 # criada
├── skills/
│   ├── README.md
│   ├── ... (skills originais)
│   └── vulnerability-analysis/
│       ├── SKILL.md                           # criada
│       └── README.md                          # criada
├── lab/
│   ├── README.md
│   ├── app.py                                 # vulnerável
│   └── app_fixed.py                           # corrigido
├── evidence/                                  # validação
└── docs/
```

---

## 📚 Referências

- [Repositório base do DIO Agent](https://github.com/digitalinnovationone/dio-agent)
- [DIO](https://dio.me)
- [MITRE ATT&CK — T1190](https://attack.mitre.org/techniques/T1190/)
- [CWE-89 — SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

<div align="center">
  Feito com 🧠, ☕ e responsabilidade — <strong>DIO Cybersecurity</strong>
</div>
