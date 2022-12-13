from lecture.live.lecture_08.ingredient import Ingredient
import pickle


class Repository:
    def __init__(self):
        self._data = {}

    def add(self, ingredient):
        if type(ingredient) != Ingredient:
            raise TypeError("Can only add ingredients to repo!")
        if ingredient.id in self._data:
            raise ValueError("Ingredient already added")
        self._data[ingredient.id] = ingredient

    def get(self, ingr_id):
        return self._data[ingr_id]

    def __len__(self):
        return len(self._data)


"""
This repository stores data in memory. Let's add a few ingredients
"""
# repo = Repository()
# repo.add(Ingredient(100, "Flour"))
# repo.add(Ingredient(101, "Spices"))
# print(repo.get(101))
# print(len(repo))

"""
We want to save all changes to a file.
We want to use both memory-repo and file-repo
We don't want to duplicate code :) 
We want to allow new file-based repo implementations 
"""


# fileRepository inherits from Repository
# it has all fields and methods of Repository
class fileRepository(Repository):
    def __init__(self):
        # call base class constructor
        super().__init__()
        # load input file
        self._load_file()

    # NOTE - this is a Template Method design pattern
    def add(self, ingredient):
        # do everything the parent's add() does
        super().add(ingredient)
        # save the ingredients to file
        self._save_file()

    def _load_file(self):
        raise NotImplementedError()

    def _save_file(self):
        raise NotImplementedError()


# code below cannot work due to NotImplementedError
# repo = fileRepository()
# repo.add(Ingredient(100, "Flour"))
# repo.add(Ingredient(101, "Spices"))
# print(repo.get(101))
# print(len(repo))

"""
Create a binary file repo that DOES work
"""


class binFileRepository(fileRepository):
    def _load_file(self):
        fin = open("repo.bin", "rb")
        self._data = pickle.load(fin)
        fin.close()

    def _save_file(self):
        # w -write, b - binary
        fout = open("repo.bin", "wb")
        pickle.dump(self._data, fout)
        fout.close()


if __name__ == "__main__":
    repo = binFileRepository()
    # repo.add(Ingredient(100, "Flour"))
    # repo.add(Ingredient(101, "Spices"))
    print(repo.get(101))
    print(len(repo))
