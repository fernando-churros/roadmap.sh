import json
from CreateTask import CreateTask

class Crud:
    file_json = 'dados.json'

    def __init__(self):
        self.tasks = self.all_tasks()

    def add(self, other) -> None:
        other.id = self.create_id()
        self.tasks.append(other)

    def delete(self, value):
        is_deleted:bool = False

        for item in self.tasks:
            if item.id == value:
                self.tasks.remove(item)
                is_deleted = True
                break

        if not is_deleted:
            raise ValueError('Tarefa não encontrada')

    def update(self, value:int, new_status:int):
        (is_valid, task) = self.search_id(value)

        if not is_valid:
            raise ValueError('Tarefa não encontrada')

        status:str = 'todo'
        match new_status:
            case 1:
                pass
            case 2:
                status = 'in-progress'
            case 3:
                status = 'done'

        task.update_status(status)

    def list_all(self):
        x = []
        for other in self.tasks:
            x.append(other)
        return x

    def list_one(self, value) -> object:
        is_valid, task = self.search_id(value)
        return task

    def search_id(self, value) -> tuple[bool, object]:
        is_search = False

        task = None
        for x in self.tasks:
            if x.id == value:
                task = x
                is_search = True
                break

        if task is None:
            raise RuntimeError('Tarefa não localizada')

        return is_search, task

    def write_json(self):
        json_file = []
        for x in self.tasks:
            json_file.append(x.to_dict())

        with open(self.file_json, 'w', encoding='utf-8') as f:
            json.dump(json_file, f, indent=2, ensure_ascii=False)

    def create_id(self) -> int:
        if len(self.tasks) != 0:
            id_task = max(task.id for task in self.tasks) + 1
        else:
            id_task = 1

        return id_task

    def all_tasks(self) -> list:
        try:
            list_object = []

            with open(self.file_json, "r", encoding="utf-8") as f:
                x = json.load(f)

            if len(x) != 0:
                for y in x:
                    i = CreateTask(
                        y['nome'],
                        y['descrição'],
                        y['id'],
                        y['data de criação'],
                        y['ultima modificação'],
                        y['status']
                    )

                    list_object.append(i)

            return list_object
        except FileNotFoundError:
            with open(self.file_json, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2, ensure_ascii=False)
            x = []

        return x
