from lecture.live.lecture_09_10.domain.ingredient import Ingredient
from lecture.live.lecture_09_10.repo.file_repo import FileRepo
from lecture.live.lecture_09_10.repo.mem_repo import RepositoryError


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

        # NOTE PyCharm highlights the lines variable below, as it is initially defined in the try ... except block.
        # In case an IOError that is NOT a FileNotFoundError is raised, the variable remains undefined :)
        for line in lines:
            tokens = line.split(",")
            self.add(Ingredient(int(tokens[0].strip()), tokens[1].strip()))
