from domain.validators import TaskValidator, PersonValidator, AssignmentValidator
from repository.person_repository import PersonFileRepository
from repository.task_repository import TaskInMemoryRepository, TaskFileRepository
from repository.assignment_repository import AssignmentInMemoryRepository
from service.assignment_service import AssignmentService
from service.person_service import PersonController
from service.task_service import TaskController
from ui.console import Console

# task_repository = TaskInMemoryRepository()
task_repository = TaskFileRepository("data/tasks.txt")
person_repository = PersonFileRepository('data/persons.txt')
assignment_repository = AssignmentInMemoryRepository()

task_validator = TaskValidator()
person_validator = PersonValidator()
assignment_validator = AssignmentValidator()

task_service = TaskController(task_repository, task_validator)
person_service = PersonController(person_repository, person_validator)
assignment_service = AssignmentService(task_repository, person_repository, assignment_repository,
                                          assignment_validator)


console = Console(task_service, person_service, assignment_service)
console.run()
