from lecture.live.lecture_09_10.domain.idobject import IdObject
from lecture.live.lecture_09_10.domain.ingredient import Ingredient
from lecture.live.lecture_09_10.domain.product import Product
from lecture.live.lecture_09_10.domain.recipe import Recipe
from lecture.live.lecture_09_10.domain.stock import Stock
from lecture.live.lecture_09_10.repo.converters import StockConverter
from lecture.live.lecture_09_10.repo.ingredient_repo import IngredientFileRepo
from lecture.live.lecture_09_10.repo.product_repo import ProductFileRepo
from lecture.live.lecture_09_10.repo.recipe_repo import RecipeFileRepo
from lecture.live.lecture_09_10.repo.stock_repo import StockFileRepo
from lecture.live.lecture_09_10.repo.mem_repo import Repository
from lecture.live.lecture_09_10.repo.text_file_repo import TextFileRepo


def create_ingredients():
    ingr = {}
    ingr[100] = Ingredient(100, "Bread Flour (White 550)")
    ingr[101] = Ingredient(101, "Yeast (dry)")
    ingr[102] = Ingredient(102, "Sugar (white)")
    ingr[103] = Ingredient(103, "Salt (regular)")
    ingr[104] = Ingredient(104, "Oil (canola)")
    ingr[105] = Ingredient(105, "Butter")
    ingr[106] = Ingredient(106, "Egg (chicken)")
    ingr[107] = Ingredient(107, "Cake flour")
    ingr[108] = Ingredient(108, "Baking powder")
    ingr[109] = Ingredient(109, "Vanilla (extract)")
    return ingr


def create_stocks():
    ingredients = create_ingredients()
    stocks = {}

    for ingredient in ingredients.values():
        stocks[ingredient.id] = Stock(ingredient.id, ingredient, 1000)
    return stocks


def create_recipes():
    ingredients = create_ingredients()

    """
    Bread

    1 package (1/4 ounce) active dry yeast
    2-1/4 cups warm water (110° to 115°)
    3 tablespoons sugar plus 1/2 teaspoon sugar
    1 tablespoon salt
    2 tablespoons canola oil
    6-1/4 to 6-3/4 cups bread flour
    source: https://www.tasteofhome.com/recipes/basic-homemade-bread/
    """
    # TODO How do we fix that Stock instances have the same id's as Ingredient instances?
    recipe_bread = Recipe(500, "Basic Homemade Bread")
    recipe_bread.stocks.append(Stock(101, ingredients[101], 20))
    recipe_bread.stocks.append(Stock(102, ingredients[102], 30))
    recipe_bread.stocks.append(Stock(103, ingredients[103], 5))
    recipe_bread.stocks.append(Stock(104, ingredients[104], 10))
    recipe_bread.stocks.append(Stock(100, ingredients[100], 1000))

    """
    Cake recipe
    
    175g (6oz) margarine or softened butter
    175g (6oz) caster sugar
    3 large eggs
    175g (6oz) self-raising flour, sifted
    1tsp baking powder
    1tsp vanilla extract
    pinch of salt
    source: https://www.houseandgarden.co.uk/recipe/simple-vanilla-cake-recipe
    
    this recipe in CSV file format 
    501,Tasty Cookies,105,175,102,175,106,3, ...
    """
    recipe_cake = Recipe(501, "Tasty Cookies")
    recipe_cake.stocks.append(Stock(105, ingredients[105], 175))
    recipe_cake.stocks.append(Stock(102, ingredients[102], 175))
    recipe_cake.stocks.append(Stock(106, ingredients[106], 3))
    recipe_cake.stocks.append(Stock(107, ingredients[107], 175))
    recipe_cake.stocks.append(Stock(108, ingredients[108], 5))
    recipe_cake.stocks.append(Stock(109, ingredients[109], 5))
    recipe_cake.stocks.append(Stock(103, ingredients[103], 2))

    return [recipe_bread, recipe_cake]


if __name__ == "__main__":
    # 1. Ingredients
    # ingr_repo = Repository()
    ingr_repo = IngredientFileRepo()
    for i in ingr_repo:
        print(i)

    # for ingr in create_ingredients().values():
    #     ingr_repo.add(ingr)
    # print(len(ingr_repo))
    # print(ingr_repo.get(105))

    # 2. Stocks
    stock_converter = StockConverter(ingr_repo)
    stock_repo = TextFileRepo(stock_converter, file_name="stocks.txt")
    print(stock_repo.get(105).ingredient)

    for stock in stock_repo:
        print(str(stock.id) + ", " + str(stock.ingredient))

    # stock_repo = StockFileRepo(ingr_repo)
    # print(stock_repo.get(105))

    # 3. Products
    # TODO Must implement a file-backed Recipe Repository :)
    recipe_repo = RecipeFileRepo(stock_repo)
    # TODO How can we add all recipes to the repo at once?
    # recipe_repo.add(create_recipes()[0])
    # recipe_repo.add(create_recipes()[1])
    print(recipe_repo.get(501))

    product_repo = ProductFileRepo(recipe_repo)
    # product_repo.add(Product(3000, "Basic Homemade Bread", 0, recipe_repo.get(500)))
    # product_repo.add(Product(3001, "Simple Vanilla Cake", 0, recipe_repo.get(501)))

    # for stock in create_stocks().values():
    #     stock_repo.add(stock)

    # 2. Recipes
    # recipe_repo = Repository()
    # for recipe in create_recipes():
    #     recipe_repo.add(recipe)
    # print(len(recipe_repo))

    # recipes = create_recipes()
    # print(recipes)
