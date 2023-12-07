from src2023.lecture.livecoding.lecture10.repo.memory_repo import MemoryRepository


class CarService:
    def __init__(self, car_repo: MemoryRepository):
        self.__repo = car_repo
