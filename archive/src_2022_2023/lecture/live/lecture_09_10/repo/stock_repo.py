from archive.src_2022_2023.lecture.live.lecture_09_10.domain.stock import Stock
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.file_repo import FileRepo
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.mem_repo import Repository, RepositoryError


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

        # NOTE PyCharm highlights the lines variable below, as it is initially defined in the try ... except block.
        # In case an IOError that is NOT a FileNotFoundError is raised, the variable remains undefined :)
        for line in lines:
            tokens = line.split(",")
            ingr = self._ingr_repo.get(int(tokens[1].strip()))
            self.add(Stock(int(tokens[0].strip()), ingr, int(tokens[2].strip())))
