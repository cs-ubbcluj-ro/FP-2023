from repository.memory_repository import TaskInMemoryRepository
from service.service import TaskController
from src2023.seminar.group917.Seminar_9.repository.file_repository import TaskFileRepository
from ui.console import Console

#repository = TaskInMemoryRepository()
repository = TaskFileRepository("data/tasks.pickle")
controller = TaskController(repository)
console = Console(controller)
console.run()