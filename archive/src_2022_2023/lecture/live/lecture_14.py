from archive.src_2022_2023.lecture.live.lecture_09_10.repo.ingredient_repo import IngredientFileRepo

repo = IngredientFileRepo("./lecture_09_10/ingredients.txt")

data = []
for ingr in repo:
    data.append(ingr)

data.sort(key=lambda x: x.name)
for ingr in data:
    print(ingr)
#
# T(n) = 1, n <= 1
# T(n) = 4 * T(n/2), n > 1


n = 1
while n > 0:
    print(n)
    n = n / 3
