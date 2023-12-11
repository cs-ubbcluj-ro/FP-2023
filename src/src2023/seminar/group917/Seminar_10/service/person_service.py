from src2023.seminar.group917.Seminar_10.domain.person import Person
from src2023.seminar.group917.Seminar_10.domain.validators import PersonValidator


class PersonController:
    def __init__(self, repository, person_validator: PersonValidator):
        self.__person_validator = person_validator
        self.__repo = repository

    def add_person(self, cnp: str, nume: str) -> None:
        """
        Add person
        :raises: DuplicateCNPException if person with CNP already exists
        """
        person = Person(cnp, nume)
        self.__person_validator.validate(person)
        self.__repo.store(person)

    def delete_person(self, cnp: str):
        """
        Deletes person with given CNP

        :raises: PersonDoesNotExistException if person with the given CNP does not exist
        """

        return self.__repo.delete(cnp)

    def get_all_persons(self) -> list:

        return self.__repo.get_all()




