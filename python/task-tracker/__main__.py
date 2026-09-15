from Menu import Menu
from Crud import Crud
from CreateTask import CreateTask

def main():
    crud = Crud()
    while True:
        try:
            menu = Menu()
            option = menu.initial()

            match option:
                case 1:
                    menu.create()
                    task = CreateTask(str(input('Nome da tarefa: ')), str(input('Descrição da tarefa: ')) )
                    crud.add(task)

                    print('Tarefa criada')
                case 2:
                    menu.delete()
                    item = int(input('id: '))
                    crud.delete(item)

                    print('Tarefa deletada')
                case 3:
                    menu.update()
                    item = int(input('id: '))
                    new_status = int(input('status: '))
                    crud.update(item, new_status)
                    print('Tarefa atualizada')
                case 4:
                    menu.to_list()
                    option = int(input('Opção: '))

                    match option:
                        case 1:
                            item = crud.list_one(int(input('ID: ')))
                            for key, value in item.to_dict().items():
                                print(f'{key}: {value}')
                            print('-' * 50)
                        case 2:
                            item = crud.list_all()
                            for other in item:
                                for key, value in other.to_dict().items():
                                    print(f'{key}: {value}')
                                print('-' * 50)
                case 5:
                    crud.write_json()
                    print('Saindo...')
                    break

        except (ValueError, RuntimeError) as e:
            print(e)

if __name__ == "__main__":
    main()
