from typing import Any


class CreateTask:
    def __init__(self, id_task:int, name: str, desc: str, create_date, status: str = 'todo') -> None:
        self.id_task = id_task
        self.name = name
        self.desc = desc
        self.create_date = create_date
        self.status = status

    @property
    def create_date(self) -> Any:
        return self._create_date
    @create_date.setter
    def create_date(self, date) -> None:
        self._create_date = date

    @property
    def id_task(self) -> Any:
        return self._id
    @id_task.setter
    def id_task(self, id_task):
        self._id = id_task

    def to_dict(self) -> dict:
        to_dict = {
            'id': self.id_task,
            'nome': self.name,
            'descrição': self.desc,
            'data de criação': self.create_date,
            'status': self.status
        }

        return to_dict
