from random import randint

class SecretNumber:
    def __init__(self):
        self.__random_num = randint(1, 100)

    @property
    def random_num(self):
        return self.__random_num


    def __eq__(self, other):
        is_win = False

        if self.random_num == other:
            status = 'Você venceu, parabéns!'
            is_win = True
        elif self.random_num > other:
            status = 'Eu chutaria um número maior.'
        else:
            status = 'Eu chutaria um número menor.'

        print(status)
        return is_win
