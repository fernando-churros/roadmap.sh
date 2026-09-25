class GameMenu:
    def __init__(self):
        self.game_name = 'Number Guessing Game' 
        self.phrase = 'Estou pensando em um número entre 1 e 100. É capaz de adivinhar ?'
        self.separator = '-'
        self.line = len(self.phrase)
        self.__difficulty = {
            '1': ('Easy', 7),
            '2': ('Medium', 4),
            '3': ('Hard', 2),
        }
        self.__points = {
            'Easy': 0,
            'Medium': 0,
            'Hard': 0
        }

    def welcome(self):
        print(self.separator * self.line, end=' |')
        print('Estatísticas')
        print(f'{self.game_name:^{self.line}}', end=' |')
        print(f'Easy = {self.points["Easy"]}')
        print(self.separator * self.line, end=' |')
        print(f'Medium = {self.points["Medium"]}')

        print(self.phrase, end=' |')
        print(f'Hard = {self.points["Hard"]}')
        print(self.separator * self.line)

    def select_difficulty(self):
        phrase_difficulty = 'difficulty -->'
        for key, value in self.__difficulty.items():
            phrase_difficulty += f' {key} - {value[0]} [{value[1]} Chances] |'

        print(f'{phrase_difficulty} 0 - Sair do Jogo')
        try:
            difficulty = str(input('Selecione a dificuldade: '))

            if difficulty == '0':
                print('Saindo do Jogo...')
                return 'Unknown Difficulty', 0

            if not ( difficulty in self.__difficulty ): raise ValueError()

            print('Iniciando o jogo\n'.center(30))
            return self.__difficulty[difficulty][0], self.__difficulty[difficulty][1]
        except ValueError as e:
            print('Dificuldade inválida')
            return 'Unknown Difficulty', -1

    @property
    def points(self): return self.__points
    @points.setter
    def points(self, value):
        self.__points[value] += 1
