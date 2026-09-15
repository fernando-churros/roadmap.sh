# Task Tracker CLI (Python)

Aplicação interativa em Python para gerenciamento de tarefas (*Task Tracker*), permitindo cadastrar e persistir tarefas em arquivo JSON local, desenvolvida como solução para o desafio do [task-tracker](https://roadmap.sh/projects/task-tracker/solutions?u=6aa73d84c2d718138d77c38d).

---

## 📋 Sumário
- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Estrutura de Dados](#-estrutura-de-dados)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar](#-como-executar)
- [Tecnologias e Conceitos Utilizados](#-tecnologias-e-conceitos-utilizados)
- [Próximos Passos (Roadmap)](#-próximos-passos-roadmap)

---

## 📖 Sobre o Projeto

O **Task Tracker** é uma ferramenta desenvolvida com foco em conceitos fundamentais e intermediários de Python puro (sem bibliotecas externas). O sistema organiza a criação, validação e persistência de tarefas em um fluxo contínuo através de um menu interativo no terminal.

---

## ✨ Funcionalidades

- [x] **Adicionar Tarefas**: Criação de tarefas com nome e descrição validados.
- [x] **Geração Automática de IDs**: Identificadores numéricos únicos e incrementais.
- [x] **Registro de Data/Hora**: Marcação automática da data e hora de criação da tarefa.
- [x] **Validação de Entrada**: Higienização contra textos vazios e remoção de espaços duplicados.
- [x] **Persistência em JSON**: Criação automática do arquivo `dados.json` caso não exista.
- [x] **Menu Interativo**: Navegação com tratamento defensivo contra opções inválidas.
- [ ] **Atualizar Tarefas** *(em desenvolvimento)*
- [ ] **Remover Tarefas** *(em desenvolvimento)*
- [ ] **Listar Tarefas / Filtrar por Status** *(em desenvolvimento)*

---

## 📂 Estrutura do Projeto

```text
task-tracker/
├── __main__.py                   # Ponto de entrada da aplicação (loop principal)
├── CreateTask.py                 # Modelo da entidade Tarefa e suas validações
├── Crud.py                       # Camada de manipulação e regras de negócio
├── dados.py                      # Camada de persistência e leitura/escrita do JSON
├── Menu.py                       # Interface visual de menus no terminal
├── dados.json                    # Arquivo de armazenamento dos dados (gerado automaticamente)
└── requisitos_task_cli_pt_br.md  # Especificação dos requisitos do desafio
```

---

## 🗃️ Estrutura de Dados

As tarefas são armazenadas no arquivo `dados.json` seguindo o formato abaixo:

```json
[
  {
    "id": 1,
    "nome": "Estudar Python",
    "descrição": "Praticar conceitos de POO e manipulação de arquivos",
    "data de criação": "15/09/26 às 02:51",
    "status": "todo"
  }
]
```

---

## 🚀 Pré-requisitos

- **Python 3.10+** instalado (o projeto utiliza o recurso de `match/case` introduzido no Python 3.10).
- Nenhuma dependência externa necessária (apenas módulos da biblioteca padrão do Python).

---

## 💻 Como Executar

1. Abra o terminal e navegue até a pasta do projeto:
   ```bash
   cd python/task-tracker
   ```

2. Execute o módulo principal:
   ```bash
   python __main__.py
   ```
   *(ou `python3 __main__.py` dependendo do seu sistema operacional)*

3. Interaja com as opções do menu no terminal digitando o número correspondente (ex: `1` para adicionar uma tarefa, `5` para sair).

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem**: Python 3.
- **Módulos Nativos**: `json`, `datetime`, `typing`.
- **Programação Orientada a Objetos (POO)**:
  - Encapsulamento com atributos privados (`__`).
  - Métodos estáticos (`@staticmethod`) para funções utilitárias e geradores.
  - Decoradores `@property` e `@setter` para controle e validação de atributos.
- **Estruturas Modernas**: `match / case` para roteamento de opções do menu.
- **Tratamento de Exceções**: Blocos `try...except` para captura de `FileNotFoundError` e `ValueError`.
