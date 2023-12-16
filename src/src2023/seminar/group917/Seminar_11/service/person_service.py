from domain.person import Person
from domain.validators import PersonValidator
from service.undo_service import Command, Operation, CascadedOperation


class PersonController:
    def __init__(self, repository, person_validator: PersonValidator, undo_service, assignment_service):
        self.__person_validator = person_validator
        self.__repo = repository
        self.__undo_service = undo_service
        self.__assignment_service = assignment_service

    def add_person(self, cnp: str, nume: str) -> None:
        """
        Add person
        :raises: DuplicateCNPException if person with CNP already exists
        """

        person = Person(cnp, nume)
        self.__person_validator.validate(person)

        self.__repo.store(person)
        undo_action = Command(self.delete_person, cnp)
        redo_action = Command(self.add_person, cnp, person)
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record_for_undo(operation)

    def delete_person(self, cnp: str):
        """
        Deletes person with given CNP

        :raises: PersonDoesNotExistException if person with the given CNP does not exist
        """
        person_to_delete = self.__repo.get(cnp)
        undo_action = Command(self.add_person, person_to_delete.cnp, person_to_delete.name)
        redo_action = Command(self.delete_person, cnp)
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record_for_undo(operation)
        return self.__repo.delete(cnp)

    def get_all_persons(self) -> list:
        return self.__repo.get_all()
