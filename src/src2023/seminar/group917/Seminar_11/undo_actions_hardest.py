from domain.validators import PersonValidator, TaskValidator, AssignmentValidator
from print_repo_states import print_repo_contents
from repository.assignment_repository import AssignmentInMemoryRepository
from repository.person_repository import PersonInMemoryRepository
from repository.task_repository import TaskInMemoryRepository
from service.assignment_service import AssignmentService
from service.person_service import PersonController
from service.task_service import TaskController
from service.undo_service import UndoService


def undo_example_difficulty_hardest():
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

    task_service.add_task(1, 'Bake Gingerbread cookies', 24, 12, "pending")
    task_service.add_task(2, 'Make toys', 20, 12, "in-progress")

    assignment_service.create_assignment(1,1,'1100221198732',9)
    assignment_service.create_assignment(2,2,'1100221198732',10)

    print_repo_contents("Added 2 persons and 2 tasks and 2 assignments", person_repository, task_repository, assignment_repository)

    person_service.delete_person('1100221198732')
    print_repo_contents("Deleted Santa, should delete all assignments", person_repository, task_repository, assignment_repository)

    undo_service.undo()
    print_repo_contents("1 Undo. Santa should be back along with the assignments", person_repository, task_repository, assignment_repository)

    undo_service.undo()
    print_repo_contents("2 Undos. Second assignment should disappear.", person_repository, task_repository,
                        assignment_repository)

    undo_service.undo()
    print_repo_contents("3 Undos. First assignment should disappear.", person_repository, task_repository,
                        assignment_repository)

    undo_service.undo()
    print_repo_contents("4 Undos. Delete last task.", person_repository, task_repository,
                        assignment_repository)
    undo_service.undo()
    print_repo_contents("5 Undos. Delete first task.", person_repository, task_repository,
                        assignment_repository)

    undo_service.undo()
    print_repo_contents("6 Undos. Delete elves.", person_repository, task_repository,
                        assignment_repository)

    undo_service.undo()
    print_repo_contents("7 Undos. Delete Santa.", person_repository, task_repository,
                        assignment_repository)

    undo_service.redo()
    print_repo_contents("Santa is back!", person_repository, task_repository,
                        assignment_repository)

    undo_service.redo()
    print_repo_contents("Elves are back!", person_repository, task_repository,
                        assignment_repository)

    undo_service.redo()
    print_repo_contents("Task 1 back!", person_repository, task_repository,
                        assignment_repository)

    undo_service.redo()
    print_repo_contents("Task 2 back!", person_repository, task_repository,
                        assignment_repository)

    undo_service.redo()
    print_repo_contents("Assignnment 1 is back", person_repository, task_repository,
                        assignment_repository)
    undo_service.redo()
    print_repo_contents("Assignnment 2 is back", person_repository, task_repository,
                        assignment_repository)

    undo_service.redo()
    print_repo_contents("Delete Santa and its assignments", person_repository, task_repository,
                        assignment_repository)

    undo_service.undo()
    undo_service.undo()
    undo_service.undo()
    print_repo_contents("3 undos laters, should have Santa, but no assignments", person_repository, task_repository,
                        assignment_repository)

    person_service.add_person('1101213839533', 'Another elf')
    try:
        undo_service.redo()
    except:
        pass

    print_repo_contents("Repos should look the same (+1 person), redos should not have been available", person_repository, task_repository,
                        assignment_repository)


    undo_service.undo()
    print_repo_contents("Delete the second elf",
                        person_repository, task_repository,
                        assignment_repository)

    undo_service.undo()
    print_repo_contents("Delete the second task",
                        person_repository, task_repository,
                        assignment_repository)


undo_example_difficulty_hardest()
