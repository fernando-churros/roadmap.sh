class Menu:
    @staticmethod
    def menu(texto, qtd):
        print('-' * qtd)
        print(texto)
        print('-' * qtd)

    def initial(self) -> int:
        self.menu('1 Adicionar | 2 Atualizar | 3 Remover | 4 Listar | 5 Sair', 60)

        x = int(input('Opção: '))
        if not(1 <= x <= 5):
            raise ValueError('Opção inválida')

        return x

    def create(self):
        self.menu('Adicionando nova tarefa', 30)
