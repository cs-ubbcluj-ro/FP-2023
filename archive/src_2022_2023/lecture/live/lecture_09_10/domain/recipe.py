from archive.src_2022_2023.lecture.live.lecture_09_10.domain.idobject import IdObject


class Recipe(IdObject):
    # TODO What is *stocks?
    def __init__(self, _id: int, name: str, *stocks):
        super().__init__(_id)
        self._name = name
        self._stocks = list(stocks)

    @property
    def name(self):
        return self._name

    @property
    def stocks(self):
        return self._stocks

    @stocks.setter
    def stocks(self, new_value):
        self._stocks = new_value
