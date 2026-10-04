# Spec templates

Two profiles. Pick one at the start of `/tightship:spec` — the profile is a header field, not a guess made later.

- **UI** — the feature has a screen, a modal, or a form a human operates.
- **API** — the feature is an endpoint, a job, or a service contract with no screen of its own.

A feature that has both gets **two** specs (one per profile) linked to the same epic — never one hybrid
document, because the field-level detail of each profile is what makes the spec testable.

Document language follows the repo's doc language (pt-BR in these projects). **Identifiers, routes, table
and column names stay in English** — they are code.

Every section is mandatory. A section that does not apply is written as `N/A` with one line saying why.
`N/A` proves it was considered; a missing section proves nothing.

---

## Profile: UI

````markdown
# <ID> — <Verbo no infinitivo> <objeto> (<ator>)

> **Status:** rascunho
> **Perfil:** UI
> **Módulo:** <onde vive no repo>
> **Epic:** —
> **Requisitos:** FR-<AREA>-NN, NFR-<CHAR>-NN
> **Sprint:** <N>

## Acceptance Criteria

### Referência visual

<Link do protótipo/mock, ou `N/A — sem protótipo; layout definido pelas regras abaixo`>

### Especificação das telas

<Descrição do que a tela é: página, modal, drawer; o que ela mostra ao abrir; o que ela lista.>

### Caminho de menu

`Menu` → `Submenu` → `Funcionalidade`

### Perfis e privilégios

| Perfil / Ação | Privilégio | Observação |
| --- | --- | --- |
| <papel que enxerga a funcionalidade> | `<PERMISSAO>` | — |
| <ação específica> | `<PERMISSAO_ACAO>` | <o que a permissão libera> |

---

## Regras de Negócio

Numeradas, uma por comportamento. Cada regra fecha três coisas: **quando** dispara, **o que** o sistema
faz, e **qual mensagem literal** aparece (entre aspas, texto exato). Limites numéricos são números, nunca
"um limite razoável".

### 1. Restrição de Acesso

- O acesso é restrito a usuários com o privilégio `<PERMISSAO>`.
- **Validação:** <em que momento exato a permissão é verificada>. Sem a permissão, o processamento é
  bloqueado e o sistema exibe:
  > "<mensagem literal>"

  com redirecionamento para <destino>.

#### Origem do fluxo

<De onde o usuário chega nesta tela — a listagem, a ação de menu, a estória anterior.>

### 2. <Próxima regra>

### N. Persistência e Auditoria

- **Fronteira do usuário (visual):** <a ação que o usuário clica>.
- **Ação do sistema (interna):** grava no log de auditoria *quem fez* (usuário/IP), *o que fez*
  (<descrição da operação e dos dados alterados>) e *quando fez* (UTC).

---

## Cenários de Aceite (Gherkin)

Cobertura mínima: **1 caminho feliz**, **1 alternativo por comportamento dinâmico** e **1 exceção por
regra que pode falhar**. Uma regra de negócio sem cenário correspondente é uma regra não testável.

### Cenário 1 — <nome> (caminho feliz)

```gherkin
Dado que <estado inicial e permissão>
E <precondição>
Quando <ação do usuário>
Então <resultado observável>
E <efeito colateral: persistência, mensagem, redirecionamento>
```

### Cenário 2 — <nome> (caminho alternativo)

### Cenário 3 — <nome> (caminho de exceção)

---

## Dicionário de Dados de Tela (Campos)

| Nome do Campo | Tipo | Habilitado | Obrigatório | Regra / Validação |
| --- | --- | --- | --- | --- |
| `<Rótulo exibido>` | <Dropdown / Texto (N) / Data / Checkbox> | Sim / Não / Condicional (<condição>) | Sim / Não / Condicional | <origem dos dados, domínio, ordenação, limite, máscara> |

## Ações de Tela

| Nome da Ação | Destino / Ação | Regra de Ativação | Mensagens Associadas |
| --- | --- | --- | --- |
| <Rótulo do botão> | <o que executa e para onde vai> | <sempre habilitado / condição / permissão exigida> | Sucesso: "<literal>" · Erro: "<literal>" |

---

## Impacto na arquitetura

<Os building blocks, cenários de runtime, deployment e conceitos de `docs/architecture/` que esta
feature cria ou altera — cada um pelo nome usado no mapa.>

## Impacto no modelo de dados

<As entidades, atributos, relações e arquivos/tabelas de `docs/data-model/` que esta feature cria ou
altera, ou `N/A — <por quê>`.>

## Fora de Escopo

- <O que esta spec deliberadamente não cobre, e onde isso será tratado.>

## Quebra em Tasks

| # | Título | Escopo | Critério de aceite | Depende de |
| --- | --- | --- | --- | --- |
| 1 | <título imperativo da issue> | <arquivos/camada que a task toca> | <Cenário N, ou regra N verificada> | — |
| 2 | <...> | <...> | <...> | 1 |
````

---

## Profile: API

````markdown
# <ID> — <Verbo no infinitivo> <recurso>

> **Status:** rascunho
> **Perfil:** API
> **Módulo:** <onde vive no repo>
> **Epic:** —
> **Requisitos:** FR-<AREA>-NN, NFR-<CHAR>-NN
> **Sprint:** <N>

## Acceptance Criteria

### Contrato

| Método | Rota | Auth / Role | Idempotente |
| --- | --- | --- | --- |
| `POST` | `/v1/<resource>` | `<ROLE>` | Sim / Não |

### Request

| Campo | Tipo | Obrigatório | Validação |
| --- | --- | --- | --- |
| `field` | `string` | Sim | <limite, formato, domínio> |

```json
{ "field": "exemplo" }
```

### Response

**`201 Created`**

```json
{ "id": "uuid", "field": "exemplo" }
```

| Status | Quando |
| --- | --- |
| `201` | <condição> |
| `400` | <condição> |
| `403` | <condição> |

### Perfis e privilégios

| Papel | Permissão | Observação |
| --- | --- | --- |
| <papel> | `<PERMISSAO>` | <o que libera> |

---

## Regras de Negócio

Mesma disciplina do perfil UI: numeradas, com o gatilho, o efeito e a mensagem literal de erro.

### 1. Autorização

<Quem pode chamar, em que momento a checagem acontece, o que acontece sem permissão.>

### 2. <Regra de domínio>

### N. Persistência e Auditoria

- **Tabelas/colunas alteradas:** <lista>.
- **Auditoria:** grava *quem* (usuário/IP), *o quê* (<operação e dados>) e *quando* (UTC).
- **Eventos/integrações disparados:** <lista, ou `N/A`>.

---

## Erros

| Código | HTTP | Quando | Mensagem |
| --- | --- | --- | --- |
| `<CODIGO_ERRO>` | `400` | <condição exata> | "<mensagem literal>" |

## Efeitos Colaterais

- **Persistência:** <o que grava, em qual estado>
- **Concorrência:** <o que acontece se o estado mudar entre a leitura e a gravação>
- **Transação:** <o que é atômico com o quê>

---

## Cenários de Aceite (Gherkin)

Cobertura mínima: **1 caminho feliz**, **1 por erro da tabela acima**, **1 de autorização negada**.

### Cenário 1 — <nome> (caminho feliz)

```gherkin
Dado que <ator> possui a permissão <PERMISSAO>
E <estado do recurso>
Quando envia `POST /v1/<resource>` com <payload>
Então o sistema responde `201`
E persiste <o quê, em que estado>
E grava a operação no log de auditoria
```

### Cenário 2 — <nome> (exceção)

---

## Impacto na arquitetura

<Os building blocks, cenários de runtime, deployment e conceitos de `docs/architecture/` que esta
feature cria ou altera — cada um pelo nome usado no mapa.>

## Impacto no modelo de dados

<As entidades, atributos, relações e arquivos/tabelas de `docs/data-model/` que esta feature cria ou
altera, ou `N/A — <por quê>`.>

## Fora de Escopo

- <O que esta spec deliberadamente não cobre.>

## Quebra em Tasks

| # | Título | Escopo | Critério de aceite | Depende de |
| --- | --- | --- | --- | --- |
| 1 | <título imperativo da issue> | <arquivos/camada que a task toca> | <Cenário N verificado> | — |
````

---

## Writing the task breakdown

The breakdown table is the contract `/tightship:epic` publishes verbatim — it does not re-read the spec to invent
tasks. So the table has to hold up on its own:

- **One task = one delivery**: a sub-issue and one commit on the epic's branch, sized to be reviewed in
  one sitting. If a task cannot be verified without another task's code, it is half of one — merge
  them. A task too small to be worth its own review cycle joins its neighbour.
- **Order by dependency.** `Depende de` carries task numbers, never prose.
- **Every acceptance scenario in the spec maps to at least one task.** A scenario nobody owns is a feature
  nobody builds.
- Slice vertically along the repo's own architecture: one behavior through every part it crosses beats
  one part for every behavior.
