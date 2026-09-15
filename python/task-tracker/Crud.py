import json
from dados import all_tasks, file_json

class Crud:
    def __init__(self):
        self.tasks = all_tasks()

    def add(self, other) -> None:
        self.tasks.append(other.to_dict())

        with open(file_json, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)
