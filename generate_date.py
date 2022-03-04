from random import randint, choice
import json

from app import Event


class GenerateData:
    def __init__(self):
        self.title = ['piwo', 'wino', 'wódkę']
        self.location = ['berlin', 'tokyo', 'donbas']
        self.duration = randint(15, 599)
        self.users = ['ala', 'ola', 'ela', 'ula', 'roman']

        self.__dupa = 'private - name mangling' # nie uzywać
        self.__dupa = 'protected' # używamy tylko w funkcji
        self.dupa = 'public'
        self.DUPA1 = 'read_only'

    @staticmethod
    def _start_time_generator():
        return f'{randint(1, 28)}-{randint(3, 12)}-{randint(2022, 2050)} {randint(1, 23)}:{randint(0, 59)}'


    def generate(self, amount, path):
        temp = []
        for i in range(amount):
            temp.append({
                'title': choice(self.title),
                'location': choice(self.location),
                'start_time': str(self._start_time_generator()),
                'duration': randint(15, 600),
                'owner': choice(self.users),
                'participants': [choice(self.users) for _ in range(randint(1, (len(self.users) - 1)))]
            })

        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(temp, file)

    @staticmethod
    def load(path):
        with open(path, 'r') as file:
            return json.load(file)

    def __repr__(self):
        attr = ', '.join(f'{k if k[0] != "_" else k[1:]}={v}' for k, v in self.__dict__.items())
        return f"{type(self).__name__}({attr})"
