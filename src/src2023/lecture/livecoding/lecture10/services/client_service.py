from src2023.lecture.livecoding.lecture10.repo.memory_repo import MemoryRepository


class ClientService:
    def __init__(self, client_repo: MemoryRepository):
        if not isinstance(client_repo, MemoryRepository):
            raise TypeError("Must have a MemoryRepository")
        self.__repo = client_repo
