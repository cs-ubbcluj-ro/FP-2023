from archive.src_2022_2023.lecture.live.lecture_09_10.domain.product import Product
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.file_repo import FileRepo
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.mem_repo import Repository


class ProductFileRepo(FileRepo):
    def __init__(self, recipe_repo: Repository, file_name="products.txt"):
        self._file_name = file_name
        self._recipe_repo = recipe_repo
        super().__init__()

    def _save_file(self):
        fout = open(self._file_name, "wt")
        for product in self._data.values():
            line = str(product.id) + "," + str(product.name) + "," + str(product.quantity) + "," + str(
                product.recipe.id) + "\n"
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
            recipe = self._recipe_repo.get(int(tokens[3].strip()))
            self.add(Product(int(tokens[0].strip()), tokens[1].strip(), int(tokens[2].strip()), recipe))
