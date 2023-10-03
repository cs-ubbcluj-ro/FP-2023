"""
Created on Nov 22, 2016

@author: Arthur
"""
import pickle


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


def write_binary_file(file_name, persons):
    f = open(file_name, "wb")
    pickle.dump(persons, f)
    f.close()


def read_binary_file(file_name):
    try:
        f = open(file_name, "rb")
        return pickle.load(f)
    except EOFError:
        """
            This is raised if input file is empty
        """
        return []
    except IOError as e:
        """
            Here we 'log' the error, and throw it to the outer layers 
        """
        print("An error occured - " + str(e))
        raise e


if __name__ == "__main__":
    """
        Initialize a list of objects
    """
    persons = [Person(1, "Pop", "Anca"), Person(2, "Morariu", "Sergiu"), Person(3, "Moldovean", "Iuliu")]

    """
        Write it to a text file
    """
    write_binary_file("persons.pickle", persons)

    """
        Read it back and see what we have
    """
    for p in read_binary_file("persons.pickle"):
        print(p)
