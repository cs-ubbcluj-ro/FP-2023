from lecture.live.lecture_09_10.domain.idobject import IdObject
from lecture.live.lecture_09_10.domain.ingredient import Ingredient
from lecture.live.lecture_09_10.domain.stock import Stock
from lecture.live.lecture_09_10.repo.mem_repo import Repository, RepositoryError


class FileRepo(Repository):
    def __init__(self):
        super().__init__()
        # load the file on startup
        self._load_file()

    def add(self, id_object: IdObject):
        super().add(id_object)
        # if no exceptions are raised we get here :)
        self._save_file()

    def _save_file(self):
        raise NotImplementedError()

    def _load_file(self):
        raise NotImplementedError()


class IngredientFileRepo(FileRepo):
    def __init__(self, file_name="ingredients.txt"):
        self._file_name = file_name
        super().__init__()

    def _save_file(self):
        fout = open(self._file_name, "wt")
        for ingr in self._data.values():
            line = str(ingr.id) + "," + ingr.name + "\n"
            fout.write(line)
        fout.close()

    def _load_file(self):
        try:
            fin = open(self._file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except FileNotFoundError:
            # option 1: behave like no input file is normal => empty repo
            # we eat the exception :)
            # pass
            # option 2: file must be present => program cannot make progress
            raise RepositoryError("Input file does not exit")
        except IOError:
            # NOTE FileNotFoundError is handled in the except block above here
            # NOTE IOError that are not FileNotFoundError are handled here
            pass

        for line in lines:
            tokens = line.split(",")
            self.add(Ingredient(int(tokens[0].strip()), tokens[1].strip()))


class StockFileRepo(FileRepo):
    def __init__(self, ingr_repo: Repository, file_name="stocks.txt"):
        self._file_name = file_name
        self._ingr_repo = ingr_repo
        super().__init__()

    def _save_file(self):
        fout = open(self._file_name, "wt")
        for stock in self._data.values():
            line = str(stock.id) + "," + str(stock.ingredient.id) + "," + str(stock.quantity) + "\n"
            fout.write(line)
        fout.close()

    def _load_file(self):
        try:
            fin = open(self._file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except FileNotFoundError:
            # option 1: behave like no input file is normal => empty repo
            # we eat the exception :)
            # pass
            # option 2: file must be present => program cannot make progress
            raise RepositoryError("Input file does not exit")
        except IOError:
            # NOTE FileNotFoundError is handled in the except block above here
            # NOTE IOError that are not FileNotFoundError are handled here
            pass

        for line in lines:
            tokens = line.split(",")
            ingr = self._ingr_repo.get(int(tokens[1].strip()))
            self.add(Stock(int(tokens[0].strip()), ingr, int(tokens[2].strip())))
