from repository.student_repo import StudentRepo
from service.student_service import StudentService
from ui.console import Console

repo = StudentRepo()
service = StudentService(repo)
console = Console(service)
console.run()