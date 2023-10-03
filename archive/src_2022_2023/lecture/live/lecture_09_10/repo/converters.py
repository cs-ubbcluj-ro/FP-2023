from archive.src_2022_2023.lecture.live.lecture_09_10.domain.idobject import IdObject
from archive.src_2022_2023.lecture.live.lecture_09_10.domain.stock import Stock
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.mem_repo import Repository


class Converter:
    def to_str(self, obj: IdObject):
        raise NotImplementedError()

    def from_str(self, string: str) -> IdObject:
        raise NotImplementedError()


class StockConverter(Converter):
    def __init__(self, ingr_repo: Repository):
        self._ingr_repo = ingr_repo

    def to_str(self, stock: Stock):
        return str(stock.id) + "," + str(stock.ingredient.id) + "," + str(stock.quantity)

    def from_str(self, string: str):
        tokens = string.split(",")
        return Stock(int(tokens[0].strip()), self._ingr_repo.get(int(tokens[1].strip())), int(tokens[2].strip()))
