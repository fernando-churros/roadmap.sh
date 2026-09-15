class Menu:
    @staticmethod
    def menu(texto, qtd):
        print('-' * qtd)
        print(texto)
        print('-' * qtd)

    def initial(self) -> int:
        self.menu('1 Adicionar | 2 Remover | 3 Atualizar | 4 Listar | 5 Sair', 60)

        x = int(input('Opção: '))
        if not(1 <= x <= 5):
            raise ValueError('Opção inválida')

        return x

    def create(self):
        self.menu('Adicionando nova tarefa', 30)

    def delete(self):
        self.menu('Removendo tarefa', 30)

    def update(self):
        self.menu('Atualizando tarefa\n1 todo | 2 in-progress | 3 done', 30)

    def to_list(self):
        self.menu('Listar Tarefa\n 1 - Busca única | 2 - Listagem completa', 50)