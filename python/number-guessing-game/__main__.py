import os
from time import sleep
from SecretNumber import SecretNumber
from GameMenu import GameMenu

def main():
    menu = GameMenu()

    while True:
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        menu.welcome()

        (difficulty_name, attempt_limit) = menu.select_difficulty()

        if attempt_limit == 0: return

        if attempt_limit == -1:
            continue

        print(f'DIFICULDADE: {difficulty_name}')
        secret_number = SecretNumber()

        i = 1
        while i <= attempt_limit:
            print(f'Tentativa Nº{i}')
            try:
                answer_user = int(input('Qual é o seu palpite: '))

                if not (1 <= answer_user <= 100):
                    print('Apenas números entre 1 e 100!')
                    continue

                if secret_number == answer_user:
                    menu.points = difficulty_name
                    break

                i += 1
            except ValueError as e:
                print('Escolha números inteiros dentro do range.')
        else:
            print('Você perdeu')

if __name__ == '__main__':
    main()