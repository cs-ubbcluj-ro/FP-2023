# Ciupe Marius Daniel
import random

from src2023.lecture.livecoding.lecture10.domain.idobject import IdObject


class Client(IdObject):
    def __init__(self, _id: int, name: str):
        super().__init__(_id)
        if not isinstance(name, str):
            raise TypeError("Name must be of type str.")
        self.__name = name

    def __str__(self):
        return f'ID: {self.id}; Name: {self.name}'

    def __eq__(self, other):
        return self.id == other.id

    @property
    def name(self):
        return self.__name


def generate_clients(n: int) -> list:
    _id = 200
    family_names = ['Smith', 'Jones', 'Williams', 'Taylor', 'Brown', 'Wilson', 'Davies', 'Evans', 'Thomas', 'Johnson']
    given_names = ["Oliver", "William", "Jack", "Harry", "Leo", "Olivia", "Amelia", "Evelyn", "Grace", "Sophie"]
    result = []
    for i in range(n):
        result.append(Client(_id + i, random.choice(family_names) + " " + random.choice(given_names)))
    return result

# for c in generate_clients(5):
#     print(c)