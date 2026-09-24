from random import randint

class SecretNumber:
    def __init__(self):
        self.__random_num = randint(1, 100)

    def __eq__(self, other):
        if self.__random_num == other:
            return True
        return False