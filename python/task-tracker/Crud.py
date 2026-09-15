import json
from datetime import datetime
from CreateTask import CreateTask


class Crud:
    FILE_JSON = 'dados.json'

    def __init__(self):
        self.tasks = self.all_tasks()

    def add(self, name, desc) -> None:
        x: datetime = datetime.now()
        create_date = x.strftime('%d/%m/%y ás %H:%M')
        if len(self.tasks) != 0:
            id_task = max(task['id'] for task in self.tasks) + 1
        else:
            id_task = 1

        new_task = CreateTask(id_task, name, desc, create_date)
        self.tasks.append(new_task.to_dict())

        with open(self.FILE_JSON, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)

    def all_tasks(self) -> list:
        try:
            with open(self.FILE_JSON, "r", encoding="utf-8") as f:
                x = json.load(f)

        except FileNotFoundError:
            with open(self.FILE_JSON, "w", encoding="utf-8") as f:
                json.dump([], f, indent=2, ensure_ascii=False)
            x = []

        return x
