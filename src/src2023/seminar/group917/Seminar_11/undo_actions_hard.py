from domain.validators import PersonValidator, TaskValidator, AssignmentValidator
from print_repo_states import print_repo_contents
from repository.assignment_repository import AssignmentInMemoryRepository
from repository.person_repository import PersonInMemoryRepository
from repository.task_repository import TaskInMemoryRepository
from service.assignment_service import AssignmentService
from service.person_service import PersonController
from service.task_service import TaskController
from service.undo_service import UndoService


def undo_example_difficulty_hard():
    person_repository = PersonInMemoryRepository()
    task_repository = TaskInMemoryRepository()
    assignment_repository = AssignmentInMemoryRepository()

    person_validator = PersonValidator()
    task_validator = TaskValidator()
    assignment_validator = AssignmentValidator()

    undo_service = UndoService()
    assignment_service = AssignmentService(undo_service,task_repository, person_repository, assignment_repository,
                                           assignment_validator)
    person_service = PersonController(person_repository, person_validator, undo_service, assignment_service)
    task_service = TaskController(task_repository, task_validator, undo_service, assignment_service)

    person_service.add_person("1100221198732", "Santa Claus")
    person_service.add_person("1101213139433", "Santa's elf")
    print_repo_contents("Added 2 people.", person_repository, None, None)

    task_service.add_task(1, 'Bake Gingerbread cookies', 24, 12, "pending")
    task_service.add_task(2, 'Make toys', 20, 12, "in-progress")
    print_repo_contents("Added 2 persons and 2 tasks.", person_repository, task_repository, None)


    person_service.delete_person('1101213139433')
    print('Delete person',undo_service)
    task_service.delete_task(2)
    print('After 2 person additions, 2 task additions, 1 person deletion and 1 task deletion')
    print(undo_service)
    print_repo_contents("Oh no! Deleted Santa's elves. Also deleted the task of making toys. What will happen with Christmas?", person_repository,
                        task_repository, None)

    undo_service.undo()
    print(undo_service)
    print_repo_contents("1 Undo. Toys should be on the agenda.", person_repository,
                        task_repository, None)

    undo_service.undo()
    print(undo_service)
    print_repo_contents("2 Undos. The elves have returned!.", person_repository,
                        task_repository, None)

    undo_service.redo()
    print_repo_contents("1 redo. Someone is intent on ruining Christmas...elves should go *poof*. ", person_repository,
                        task_repository, None)

    undo_service.redo()
    print_repo_contents("2 redo. Of course, now no toys... ", person_repository,
                        task_repository, None)

    #This should throw an error
    undo_service.redo()



undo_example_difficulty_hard()