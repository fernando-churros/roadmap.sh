class GameMenu:
    def __init__(self):
        self.game_name = 'Number Guessing Game' 
        self.phrase = 'Estou pensando em um número entre 1 e 100. É capaz de adivinhar ?'
        self.separator = '-'
        self.line = len(self.phrase)
        self.difficulty = {
            '1': ('Easy', 7),
            '2': ('Medium', 4),
            '3': ('Hard', 2),
        }

    def welcome(self):
        print(self.separator * self.line)
        print(f'{self.game_name:^{self.line}}')
        print(self.separator * self.line)

        print(self.phrase)
        print(self.separator * self.line)

    def select_difficulty(self):
        phrase_difficulty = 'difficulty -->'
        for key, value in self.difficulty.items():
            phrase_difficulty += f' {key} - {value[0]} [{value[1]} Chances] |'

        print(f'{phrase_difficulty} 0 - Sair do Jogo')
        try:
            difficulty = str(input('Selecione a difuculdade: '))

            if int(difficulty) == 0:
                print('Saindo do Jogo...')
                return 'Unknown Difficulty', 0

            if not ( 1 <= int(difficulty) <= 3 ): raise ValueError()

            print('Iniciando o jogo\n'.center(30))
            return self.difficulty[difficulty][0], self.difficulty[difficulty][1]
        except ValueError as e:
            print('Dificuldade inválida')
            return 'Unknown Difficulty', 0
