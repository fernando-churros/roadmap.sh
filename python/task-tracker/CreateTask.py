from datetime import datetime
from typing import Any
from dados import all_tasks

class CreateTask:
    def __init__(self, name: str, desc: str) -> None:
        self.__id_task = self.create_id()
        self.name = name
        self.desc = desc
        self.__create_date = self.create_date()
        self.status = 'todo'

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, item):
        (is_valid, name) = self.validar_input(item)

        if not is_valid:
            raise ValueError('Nome não pode ser vazio')

        self._name = name

    @property
    def desc(self):
        return self._desc
    @desc.setter
    def desc(self, item):
        (is_valid, desc) = self.validar_input(item)

        if not is_valid:
            raise ValueError('Descrição não pode ser vazia')

        self._desc = desc

    @staticmethod
    def create_id() -> int:
        tasks = all_tasks()
        if len(tasks) != 0:
            id_task = max(task['id'] for task in tasks) + 1
        else:
            id_task = 1

        return id_task

    @staticmethod
    def create_date():
        x: datetime = datetime.now()
        create_date = x.strftime('%d/%m/%y ás %H:%M')

        return create_date

    def to_dict(self) -> dict:
        to_dict = {
            'id': self.__id_task,
            'nome': self.name,
            'descrição': self.desc,
            'data de criação': self.__create_date,
            'status': self.status
        }

        return to_dict

    @staticmethod
    def validar_input(item) -> Any:
        input_user = item.strip()
        input_user = ' '.join(input_user.split())

        if input_user == '':
            return False, input_user

        return True, input_user
