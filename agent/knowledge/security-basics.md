# Fundamentos de segurança para o DIO Agent

Use este arquivo quando a conversa envolver vulnerabilidades, ameaças, risco, análise de código ou orientações de defesa. Ele dá vocabulário e critérios — não substitui a skill `vulnerability-analysis`, que dá o processo.

## Vulnerabilidade, ameaça e risco

| Conceito | O que é | Exemplo |
|----------|---------|---------|
| **Vulnerabilidade** | Fraqueza no código, configuração ou processo | Consulta SQL montada por concatenação de entrada do usuário |
| **Ameaça** | Algo que pode explorar a fraqueza | Ator remoto com ferramenta automatizada; insider; malware |
| **Risco** | Chance de a ameaça explorar a vulnerabilidade × impacto | Vazamento do banco de usuários em app exposta à internet |

Fórmula mental: **risco ≈ probabilidade × impacto**. Severity é a prioridade que damos a esse risco.

> Uma vulnerabilidade sem ameaça plausível é um achado, não necessariamente um incêndio. Uma ameaça sem vulnerabilidade também não gera risco. O agente deve sempre explicar os dois lados.

## A tríade CIA

- **Confidencialidade:** só quem deve ver, vê. Vazamento de senhas, tokens ou PII quebra esse pilar.
- **Integridade:** o dado não é alterado sem autorização. Injeção que modifica registros ou HTML quebra esse pilar.
- **Disponibilidade:** o serviço continua acessível. Um loop infinito, travamento ou exclusão de dados quebra esse pilar.

Toda análise deve dizer **qual pilar** foi afetado. Isso transforma "código feio" em impacto de negócio.

## Vocabulário útil (use com cuidado)

- **CWE:** catálogo de fraquezas de software (ex.: CWE-89 = SQL Injection).
- **CVE:** identificador de uma vulnerabilidade específica já divulgada em produto/versão.
- **CVSS:** sistema de pontuação de severidade. Só calcule com o vetor completo; não invente nota.
- **MITRE ATT&CK:** matriz de táticas e técnicas usadas por adversários. Exemplo: **T1190 — Exploit Public-Facing Application** para exploração de aplicação exposta. Cite só quando o cenário combinar.
- **OWASP Top 10:** lista de riscos mais comuns em aplicações web. É um ótimo ponto de partida para estudar, não um checklist definitivo.

## Boas práticas que o agente deve orientar

### No código

- **Separar código de dados:** queries parametrizadas/prepared statements em vez de concatenação.
- **Validar na entrada, codificar na saída:** whitespace, tipo, tamanho e formato; escapar HTML no ponto de saída.
- **Nunca confiar no cliente:** validação no navegador é conveniência, não segurança.
- **Autenticação e autorização separadas:** saber quem é ≠ saber o que pode fazer.
- **Senhas:** hash com salt (bcrypt/Argon2/PBKDF2), nunca texto puro, nunca MD5/SHA1.
- **Segredos fora do código:** variáveis de ambiente ou cofre; rotacionar se vazaram.
- **Mensagens de erro genéricas:** não revelar stack trace, versão ou estrutura de banco ao usuário.

### Na infraestrutura

- **Menor privilégio:** usuário de aplicação sem permissão de admin do banco ou do SO.
- **Defesa em profundidade:** firewall, WAF, segmentação de rede, _rate limiting_, monitoramento.
- **Atualizações:** manter sistema, runtime e dependências com patches.
- **Backup 3-2-1:** 3 cópias, 2 mídias diferentes, 1 offline/imutável.
- **Logs e alertas:** registrar tentativas de login e mudanças sensíveis sem vazar segredos.

### No processo

- **Revisão de código** com olhar de segurança antes de merge.
- **Testes automatizados** de comportamento inseguro e de regressão.
- **Autorização explícita** antes de qualquer teste invasivo. Laboratório isolado primeiro.

## Como o agente deve responder

- Comece pelo contexto, não pelo comando.
- Diga qual pilar CIA foi afetado e por quê.
- Explique o mecanismo antes de mostrar a correção.
- Se não souber o ID exato de uma técnica, fale que não tem certeza.
- Reforce que testes só em ambiente autorizado.
