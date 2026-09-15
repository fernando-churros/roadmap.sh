from Menu import Menu
from Crud import Crud
from CreateTask import CreateTask

def main():
    while True:
        try:
            menu = Menu()
            option = menu.initial()

            match option:
                case 1:
                    menu.create()
                    task = CreateTask(str(input('Nome da tarefa: ')), str(input('Descrição da tarefa: ')) )
                    Crud().add(task)

                    print('Tarefa criada')
                case 5:
                    print('Saindo...')
                    break

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
