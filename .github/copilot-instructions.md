# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Conventional Commits (obrigatório para mensagens de commit)

Sempre gere mensagens de commit seguindo o Conventional Commits.

Formato:
<type>(<scope>): <subject>

Regras principais:
- use tipos em minúsculas (feat, fix, docs, etc.);
- scope é opcional e não deve conter espaços;
- subject em tempo imperativo e sem ponto final;
- limite ~50 caracteres para o subject, corpo opcional para detalhes.

Tipos comuns:
- feat: nova funcionalidade
- fix: correção de bug
- docs: documentação
- style: formatação/código sem lógica
- refactor: refatoração sem alterar comportamento
- perf: melhoria de performance
- test: adicionar/alterar testes
- chore: tarefas de manutenção
- build: alterações no sistema de build
- ci: alterações em CI/CD
- revert: reverte um commit anterior

Exemplos:
- feat(auth): add OAuth2 login
- fix(api): handle null response from gateway
- docs(readme): update installation instructions
- style(lint): apply eslint autofix
- refactor(ui): simplify header component
- perf(cache): improve lookup performance
- test(auth): add unit tests for token refresh
- chore(deps): bump lodash to 4.17.21
- ci(github-actions): add release workflow
- revert: revert "feat(login): add oauth"