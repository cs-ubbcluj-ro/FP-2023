class Ingredient:
    def __init__(self, id, name):
        """
        How do we protect class fields from changes?

        C++/Java/C# -> private (just inside the class)
                       protected (inside the class and derived classes)
                       public (everywhere)
                       // default (Java), internal (C#)

        Python
            public      -> <name> (e.g., class.field_name)
            protected   -> _<name> (e.g., class._field_name)
            private     -> __<name> (e.g., class.__field_name) -> Python name mangling
        """
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        if len(new_value) < 5:
            raise ValueError("Name must have at least length 5")
        self.__name = new_value

    def __str__(self):
        return str(self.id) + " -> " + self.name


if __name__ == "__main__":
    ingr = Ingredient(100, "Random Ingredient")
    flour = Ingredient(101, "Flour")
    ingr.x = 123

    # print(ingr.__dict__)
    # print(flour.__dict__)
    # print( isinstance(ingr,Ingredient))
    # print( isinstance(ingr,str))
    # print(type(ingr) == str)
    # data = list()

    # print(ingr.x)

    # print(ingr.__id, ingr.__name)

    print(ingr)
    # print(Ingredient.get_name(ingr))

    ingr.name = "Magical ingredient"
    # ingr.id = 123
    print(ingr.id, ingr.name)
    print(ingr)
    # print(ingr.__id, ingr.__name)

    # print(flour.x)

    # print(type(ingr))
    # print(type(data))
