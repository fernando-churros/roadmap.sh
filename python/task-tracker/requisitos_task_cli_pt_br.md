# Requisitos

A aplicação deve ser executada pela linha de comando, aceitar ações e entradas do usuário como argumentos e armazenar as tarefas em um arquivo JSON. O usuário deve ser capaz de:

- Adicionar, atualizar e excluir tarefas
- Marcar uma tarefa como **em andamento** ou **concluída**
- Listar todas as tarefas
- Listar todas as tarefas que estão concluídas
- Listar todas as tarefas que não estão concluídas
- Listar todas as tarefas que estão em andamento

## Restrições

- Você pode usar qualquer linguagem de programação para desenvolver este projeto.
- Use argumentos posicionais na linha de comando para receber as entradas do usuário.
- Use um arquivo JSON para armazenar as tarefas no diretório atual.
- O arquivo JSON deve ser criado caso não exista.
- Use o módulo nativo de sistema de arquivos da linguagem de programação escolhida para interagir com o arquivo JSON.
- Não use bibliotecas ou frameworks externos para desenvolver este projeto.
- Certifique-se de tratar erros e casos extremos de maneira adequada.

## Exemplo

A lista de comandos e seus respectivos usos é apresentada abaixo:

```bash
# Adicionando uma nova tarefa
task-cli add "Comprar mantimentos"
# Saída: Tarefa adicionada com sucesso (ID: 1)

# Atualizando e excluindo tarefas
task-cli update 1 "Comprar mantimentos e preparar o jantar"
task-cli delete 1

# Marcando uma tarefa como em andamento ou concluída
task-cli mark-in-progress 1
task-cli mark-done 1

# Listando todas as tarefas
task-cli list

# Listando tarefas por status
task-cli list done
task-cli list todo
task-cli list in-progress
```

## Propriedades das tarefas

Cada tarefa deve possuir as seguintes propriedades:

- `id`: Um identificador único para a tarefa
- `description`: Uma descrição curta da tarefa
- `status`: O status da tarefa (`todo`, `in-progress`, `done`)
- `createdAt`: A data e hora em que a tarefa foi criada
- `updatedAt`: A data e hora em que a tarefa foi atualizada pela última vez

Certifique-se de adicionar essas propriedades ao arquivo JSON ao criar uma nova tarefa e atualizá-las quando uma tarefa for modificada.
