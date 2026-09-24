from SecretNumber import SecretNumber
from GameMenu import GameMenu

def main():
    menu = GameMenu()
    secret_number = SecretNumber()

    menu.welcome()
    (difficulty_name, attempt_limit) = menu.select_difficulty()

    if attempt_limit == 0: return

    print(f'DIFICULDADE: {difficulty_name}')
    for i in range(1, attempt_limit + 1):
        print(f'Tentativa Nº{i}')
        try:
            answer_user = int(input('Qual é o seu palpite: '))
        except ValueError as e:
            print('Escolha números inteiros dentro do range.')

if __name__ == '__main__':
    main()