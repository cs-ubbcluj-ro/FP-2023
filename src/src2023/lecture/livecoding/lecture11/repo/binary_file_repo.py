import pickle

from src2023.lecture.livecoding.lecture10.domain.car import generate_cars
from src2023.lecture.livecoding.lecture10.domain.idobject import IdObject
from src2023.lecture.livecoding.lecture10.repo.memory_repo import MemoryRepository


class BinaryFileRepo(MemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load()

    def __save(self):
        f = open(self.__file_name, "wb")
        pickle.dump(self._data, f)
        f.close()

    def __load(self):
        # 1. make self.__data protected => self._data
        # 2. use add from super class
        try:
            f = open(self.__file_name, "rb")
            self._data = pickle.load(f)
            f.close()
        except FileNotFoundError:
            self._data = {}

    def add(self, object: IdObject):
        super().add(object)
        self.__save()

    def remove(self, _id: int) -> IdObject:
        elem = super().remove(_id)
        self.__save()
        return elem


# mr = MemoryRepository()
br = BinaryFileRepo("cars.bin")

# print(type(mr))
# print(type(br))
# print(type(mr) == type(br))
# print(isinstance(br,BinaryFileRepo))
# print(isinstance(br,MemoryRepository))

cars = generate_cars(10)
for c in cars:
    br.add(c)

print(len(br))

for car in br:
    print(car)
