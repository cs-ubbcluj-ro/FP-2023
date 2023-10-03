"""
Created on Nov 22, 2016

@author: Arthur
"""


class Person:
    def __init__(self, person_id, family_name, given_name):
        self._personId = person_id
        self._familyName = family_name
        self._givenName = given_name

    @property
    def id(self):
        return self._personId

    @property
    def family_name(self):
        return self._familyName

    @property
    def given_name(self):
        return self._givenName

    def __str__(self):
        return str(self._personId) + " - " + self._familyName + " " + self._givenName


def write_text_file(file_name, persons):
    f = open(file_name, "w")
    try:
        for p in persons:
            person_str = str(p.id) + ";" + p.family_name + ";" + p.given_name + "\n"
            f.write(person_str)
        f.close()
    except Exception as e:
        print("An error occurred -" + str(e))


def read_text_file(file_name):
    result = []
    try:
        f = open(file_name, "r")
        line = f.readline().strip()
        while len(line) > 0:
            line = line.split(";")
            result.append(Person(int(line[0]), line[1], line[2]))
            line = f.readline().strip()
        f.close()
    except IOError as e:
        """
            Here we 'log' the error, and throw it to the outer layers 
        """
        print("An error occured - " + str(e))
        raise e

    return result


if __name__ == "__main__":
    """
        Initialize a list of objects
    """
    persons = [Person(1, "Pop", "Anca"), Person(2, "Morariu", "Sergiu"), Person(3, "Moldovean", "Iuliu")]

    """
        Write it to a text file
    """
    write_text_file("persons.txt", persons)

    """
        Read it back and see what we have
    """
    for p in read_text_file("persons.txt"):
        print(p)
