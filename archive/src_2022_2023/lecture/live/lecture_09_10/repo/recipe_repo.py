from archive.src_2022_2023.lecture.live.lecture_09_10.domain.recipe import Recipe
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.file_repo import FileRepo
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.mem_repo import Repository


class RecipeFileRepo(FileRepo):
    def __init__(self, stock_repo: Repository, file_name="recipes.txt"):
        self._file_name = file_name
        self._stock_repo = stock_repo
        super().__init__()

    def _save_file(self):
        fout = open(self._file_name, "wt")
        line = ""
        for recipe in self._data.values():
            line = str(recipe.id) + "," + str(recipe.name) + ","
            for stock in recipe.stocks:
                line += str(stock.id) + "," + str(stock.quantity) + ","
            line = line[:-1]
            line += "\n"
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
            return
            # option 2: file must be present => program cannot make progress
            # raise RepositoryError("Input file does not exit")
        except IOError:
            # NOTE FileNotFoundError is handled in the except block above here
            # NOTE IOError that are not FileNotFoundError are handled here
            pass

        # NOTE PyCharm highlights the lines variable below, as it is initially defined in the try ... except block.
        # In case an IOError that is NOT a FileNotFoundError is raised, the variable remains undefined :)
        for line in lines:
            tokens = line.split(",")
            recipe_id = int(tokens[0].strip())
            recipe_name = tokens[1].strip()

            recipe = Recipe(recipe_id, recipe_name)
            for index in range(2, len(tokens) - 1, 2):
                stock_id = int(tokens[index].strip())
                stock_quantity = int(tokens[index + 1].strip())
                stock = self._stock_repo.get(stock_id)
                stock.quantity = stock_quantity
                # add stock item to recipe
                recipe.stocks.append(stock)
            self.add(recipe)
