---
description: Revisar o PR de outra pessoa — briefing (para quê / o quê / como) + achados explicados, sem o que outro PR já resolveu
argument-hint: "[número do PR ou URL] [--only sec|perf|arch|maint]"
---

Revisar o PR: $ARGUMENTS

Este comando **explica o PR antes de julgá-lo** e **nunca publica nada no GitHub**. A saída é um
briefing em PT-BR no chat, para eu ler e então comentar por conta própria. `gh pr review`,
`gh pr comment`, `gh pr merge`, `gh pr edit` e `git push` estão proibidos aqui, mesmo que a saída
pareça pedir por eles.

## Fase 0 — preparar

1. Árvore suja (`git status --porcelain` não vazio) → **parar** e dizer o que há pendente. Não
   guardar em stash, não descartar.
2. `git fetch origin --prune`.
3. `gh pr view <n> --json number,title,body,author,baseRefName,headRefName,isDraft,commits,files,closingIssuesReferences,url`.
4. Sinais de experimento — draft, dias parado, sem issue ligada, autor automatizado, pasta nova
   isolada → perguntar em uma linha se o PR é para valer antes de auditar.
5. `gh pr checkout <n>`.
6. `BASE=origin/<baseRefName>` — a base é a **declarada pelo PR**, nunca `main` presumida.
   `MERGE_BASE=$(git merge-base $BASE HEAD)`.
7. O diff de revisão é **`git diff $MERGE_BASE...HEAD`** e só ele. Nada do que a base andou depois
   entra como autoria do PR.

No fim do comando, eu fico na branch do PR — dizer isso em uma linha, para eu já poder rodar a
aplicação.

## Fase 1 — briefing

Escrito para quem nunca viu o PR. Nesta ordem:

**Para quê** — o objetivo em 2–3 linhas, tirado da descrição, da issue linkada
(`closingIssuesReferences`, lida com `gh issue view`) e das mensagens de commit. Cada afirmação sai
marcada `[declarado]` quando veio do autor ou `[inferido]` quando foi deduzida do diff. Nunca
apresentar dedução do diff como intenção declarada do autor.

**O que mudou** — por módulo ou área, uma linha por grupo. Nunca uma lista de arquivos soltos.

**Como** — as decisões de implementação que o autor tomou: o padrão que escolheu, onde colocou o
código, o que reusou contra o que reescreveu, e os pontos onde teria sido razoável fazer diferente.
Esta é a seção que eu não consigo extrair sozinho lendo o diff no GitHub.

**Perfil de risco** — quantidade de arquivos, camadas atravessadas, e quais superfícies sensíveis o
PR toca: auth, autorização, migração de banco, dinheiro, env/segredos, upload, boundary
server/client.

## Fase 2 — defasagem da base

`git log --oneline $MERGE_BASE..$BASE -- <arquivos do PR>`

Lista os arquivos em que a base andou depois do ponto de partida. Serve a dois propósitos: avisar se
o PR precisa de rebase, e alimentar o filtro da Fase 4.

## Fase 3 — achados

Dispara os subagentes do `/tightship:audit` **em paralelo, numa só mensagem**, todos com o mesmo alvo:
`git diff $MERGE_BASE...HEAD`. `--only <eixo>` restringe a rodada.

| Eixo | Lente |
|---|---|
| **sec** | `tightship:security-audit` |
| **perf** | `tightship:performance-analysis` |
| **arch** | `tightship:architecture-reading` |
| **maint** | **Code I write** do contrato |

Um `general-purpose` por eixo, read-only, cada um carregando a lente antes de ler o diff.

Valem as lentes condicionais do `/tightship:audit`: contrato de API → `tightship:api-design`; camada de dados →
`tightship:database-design`; superfície de UI → `tightship:frontend-architecture`. A lente é o ângulo, nunca o teto.

## Fase 4 — filtro temporal

**Nenhum achado chega ao relatório sem passar pelos dois testes.** Este é o ponto do comando: tempo
gasto discutindo o que já foi tratado é tempo perdido.

1. **Já resolvido na base atual** — as linhas do achado mudaram entre `$MERGE_BASE` e `$BASE`?
   `git log -L<início>,<fim>:<arquivo> $MERGE_BASE..$BASE`, com `git log -S'<trecho>' $MERGE_BASE..$BASE`
   como rede para código que se moveu. Ler a mudança: se ela cobre o achado, descartar como
   *resolvido em `<sha>` (PR #N)*.
2. **Já sendo tratado em PR aberto** — `gh pr list --state open --json number,title,headRefName,files`.
   Cruzar por arquivo com os arquivos do achado; para cada PR que cruza, ler **apenas os hunks
   sobrepostos** de `gh pr diff <m>`. Se ataca o mesmo ponto, descartar como *sendo tratado em #M*.
   Um PR aberto que já ataca o problema basta — o problema já está em movimento em outro lugar.

Descartado não é apagado: vai para a seção **Descartados e por quê**, no fim do relatório, com o
motivo e a referência. Fora do caminho, mas auditável.

## Fase 5 — saída

Cada achado sobrevivente, ranqueado por severidade entre eixos e deduplicado (o mesmo código costuma
tropeçar em mais de um eixo — mantido uma vez, marcado com todos):

- **o que é** — uma frase
- **por que importa neste PR** — o efeito concreto, não a regra genérica
- **onde** — `path:linha` com o trecho
- **comentário pronto** — o texto em PT-BR para eu colar no GitHub, já no tom de review
- **escopo** — `no escopo` quando o PR causou o problema ou o tornou alcançável; `adjacente` quando é
  pré-existente e o PR só encostou. Adjacente vira issue, e quem decide sou eu — o comando propõe.

Fechar com **veredito recomendado** em uma linha: aprovar · pedir mudanças · conversar antes. É
recomendação. A ação no GitHub é sempre minha.
