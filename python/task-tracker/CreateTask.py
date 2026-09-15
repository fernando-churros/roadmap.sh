import datetime
from typing import Any
from dados import create_date
from datetime import datetime

class CreateTask:
    def __init__(self, name: str, desc: str, id_task:int = 0, c_date = None, u_date = None, status = None) -> None:
        self.id = id_task
        self.name = name
        self.desc = desc
        self.create_date = c_date
        self.update_date =  u_date
        self.status = status

    @property
    def id(self):
        return self.__id_task
    @id.setter
    def id(self, value):
        self.__id_task = value

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

    @property
    def create_date(self):
        return self.__create_date
    @create_date.setter
    def create_date(self, value):
        self.__create_date = create_date() if value is None else value

    @property
    def update_date(self):
        return self.__update_date
    @update_date.setter
    def update_date(self, value):
        self.__update_date = create_date() if value is None else value

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = 'todo' if value is None else value

    def update_status(self, value):
        self.__update_date = create_date()
        self.status = value

    def to_dict(self) -> dict:
        to_dict = {
            'id': self.id,
            'nome': self.name,
            'descrição': self.desc,
            'data de criação': self.create_date,
            'ultima modificação': self.update_date,
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
