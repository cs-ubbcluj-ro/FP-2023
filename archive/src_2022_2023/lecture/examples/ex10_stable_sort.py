from random import choice


def create_person(name: str, age: int):
    return {"name": name, "age": age}


def get_name(person: dict):
    return person["name"]


def get_age(person: dict):
    return person["age"]


def generate():
    """
    Generate some persons
    """
    result = []

    family_name = ['Popescu', 'Marian', 'Pop', 'Lazarescu', 'Dincu']
    given_name = ['Anca', 'Emilia', 'Liviu', 'Marius']
    age = [17, 18, 19, 20]

    for i in range(20):
        result.append(create_person(choice(family_name) + " " + choice(given_name), choice(age)))
    return result


'''
1. Generate people
'''
result = generate()

'''
2. First we sort the list by name (ascending)
'''
result.sort(key=lambda person: person["name"])

'''
3. Then we sort by age (descending) - the sorts are STABLE
'''
result.sort(key=lambda person: person["age"], reverse=True)

'''
4. People of the same age are ordered by name
'''
for p in result:
    print(p)
