from domain.person import Person
from domain.validators import PersonValidator, TaskValidator, AssignmentValidator
from print_repo_states import print_repo_contents
from repository.assignment_repository import AssignmentInMemoryRepository
from repository.person_repository import PersonInMemoryRepository
from repository.task_repository import TaskInMemoryRepository
from service.assignment_service import AssignmentService
from service.person_service import PersonController
from service.task_service import TaskController
from service.undo_service import UndoService


def undo_example_medium_difficulty():
    person_repository = PersonInMemoryRepository()
    task_repository = TaskInMemoryRepository()
    assignment_repository = AssignmentInMemoryRepository()

    person_validator = PersonValidator()
    task_validator = TaskValidator()
    assignment_validator = AssignmentValidator()

    undo_service = UndoService()
    assignment_service = AssignmentService(undo_service, task_repository, person_repository, assignment_repository,
                                           assignment_validator)
    person_service = PersonController(person_repository, person_validator, undo_service, assignment_service)
    task_service = TaskController(task_repository, task_validator, undo_service, assignment_service)

    person_service.add_person("2901009123456", "Maya")
    person_service.add_person("1860221198732", "Matthew")
    person_service.add_person("1801213139433", "Jack")

    print_repo_contents("Added 3 people.", person_repository, None, None)

    person_service.delete_person("2901009123456")
    person_service.delete_person("1860221198732")

    #print(undo_service)
    print_repo_contents("Deleted 2 people: Maya and Matthew.", person_repository, None, None)

    undo_service.undo()
    #print(undo_service)
    print_repo_contents("1 undo, Matthew should be back.", person_repository, None, None)

    undo_service.undo()
    #print(undo_service)
    print_repo_contents("2 undos, Maya should be back as well.", person_repository, None, None)


    print(undo_service)
    undo_service.redo()
    print_repo_contents("1 redo, Maya should appear as deleted again.", person_repository, None, None)



undo_example_medium_difficulty()
