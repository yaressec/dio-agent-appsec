# Revisão da skill pelo próprio DIO Agent

> **Método:** o Hermes não estava instalado no ambiente de validação. Este diálogo foi conduzido pelo assistente **seguindo o `SKILL.md` recém-criado**, inclusive a regra de "uma pergunta por vez" e a postura de não entregar resposta pronta. É uma simulação do comportamento esperado do agente especializado.

---

## Enunciado usado (trecho da aula)

> Estou evoluindo o DIO Agent com uma skill de análise de vulnerabilidades. Já criei a pasta da skill e o `SKILL.md`, mas não sei se o processo que escrevi está claro para um agente. Leia o meu `SKILL.md` e me pergunte, etapa por etapa, o que ficou ambíguo.
>
> Importante: não quero uma resposta pronta para copiar. Quero entender o processo e construir minha própria solução.

---

## Diálogo

**Você:** (enuncia o pedido acima)

**Agente:** Li o arquivo todo. Antes de apontar qualquer coisa, uma pergunta por vez, combinado?

Na **Regra 0, item 2**, você escreveu três confirmações na mesma instrução: origem do código, onde ele roda e quem consegue acessar. Mas o `AGENTS.md` manda fazer **uma pergunta por vez**. Como você quer que o agente resolva isso: ele faz uma pergunta só que cubra os três pontos, ou faz três rodadas separadas?

**Você:** Três rodadas separadas.

**Agente:** Anotado. Próxima pergunta: no item 2 você usa a expressão **"laboratório autorizado"**. O que conta como autorizado para você? Basta o estudante dizer "é um lab", ou você quer que ele afirme explicitamente que o ambiente é dele?

**Você:** Quero que ele confirme que é dele.

**Agente:** Bom critério. Terceira pergunta, agora sobre a **Etapa 1**: você escreveu "faça perguntas até saber o suficiente". O que seria "suficiente" na sua cabeça — quais informações, quando reunidas, autorizam o agente a parar de perguntar e começar a análise?

**Você:** Quando já sei onde roda, quem acessa e que tipo de dado está envolvido.

**Agente:** Isso dá um critério concreto. Quarta pergunta, sobre a **Etapa 2**: você deu o exemplo `CWE-89` + `T1190` para SQL Injection, mas também mandou "não inventar ID". Se o estudante descrever uma falha parecida, mas você não tiver certeza do mapeamento, o que o agente deve fazer: chutar um ID, omitir, ou dizer que não tem certeza e pedir verificação?

**Você:** Dizer que não tem certeza.

**Agente:** Certo. Quinta pergunta, sobre a **Etapa 4**: você escreveu "baixa probabilidade + alto impacto = Médio/Alto". Como o agente decide entre Médio e Alto sem cair na arbitrariedade? Qual critério você daria a ele?

**Você:** Acho que o Médio seria quando o impacto é alto mas a exploração exige muito esforço...

**Agente:** Entendi o raciocínio. Última pergunta desta rodada, sobre a **Etapa 5**: você autoriza "um exemplo limitado e rotulado como demonstração local", mas proíbe "payload pronto". Onde está a linha entre um exemplo conceitual útil e um atalho copiável para outra pessoa?

**Você:** Preciso definir isso melhor...

**Agente:** Perfeito — essa é a parte que você ainda precisa decidir, e é justamente o tipo de clareza que um agente não consegue inventar por conta própria.

---

## O que esta troca demonstra

- O agente **não corrigiu** o `SKILL.md`: ele transformou cada ponto ambíguo numa decisão do estudante.
- Respeitou a regra de **uma pergunta por vez**.
- Usou o próprio roteiro como fonte: citou Regra 0, Etapas 1, 2, 4 e 5.
- Reforçou a filosofia do DIO Agent: autonomia e entendimento acima da resposta pronta.

## Pontos levantados para o estudante decidir

| # | Seção do SKILL.md | Ambiguidade |
|---|-------------------|-------------|
| 1 | Regra 0, item 2 | três confirmações juntas × uma pergunta por vez |
| 2 | Regra 0, item 2 | o que conta como "laboratório autorizado" |
| 3 | Etapa 1 | o que é "saber o suficiente" |
| 4 | Etapa 2 | o que fazer sem certeza do ID (respondido: admitir) |
| 5 | Etapa 4 | critério para Médio vs. Alto |
| 6 | Etapa 5 | fronteira entre exemplo didático e payload copiável |

> As etapas 6, 7, 8 e o formato fixo ainda ficam para uma próxima rodada de perguntas.
