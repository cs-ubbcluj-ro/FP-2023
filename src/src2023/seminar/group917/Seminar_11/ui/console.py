from colorama import Fore, Style

from repository.repo_exceptions import RepositoryException

"""
Layered architecture
    ui  -> user interface
        -> all print/input (or all GUI windows/dialogs/menus etc)
        -> in our case we catch exception and display them here
    service
        -> below the UI layer (UI calls functions in services)
        -> does not know about the UI
        -> forward calls to repo, implement functionalities (undo/redo, statistics, etc.)
    repository 
        -> stores everything (preferably using files/SQL/noSQL)
        -> does not know about UI, services
    domain
        -> classes that we find in the problem statement (task, person, student, book, etc.)
        -> does not know about any layer
        
    function call direction:
        ui -> services -> repository
    """


class Console:
    def __init__(self, task_service, person_service,
                 assignment_service):
        self.__task_service = task_service
        self.__person_service = person_service
        self.__assignment_service = assignment_service

    def _print_available_commands(self):

        print(Fore.MAGENTA + 'add_task.' + Style.RESET_ALL + ' Add task')
        print(Fore.MAGENTA + 'del_task.' + Style.RESET_ALL + ' Delete task')

        print(Fore.MAGENTA + 'add_person.' + Style.RESET_ALL + ' Add person')
        print(Fore.MAGENTA + 'del_person.' + Style.RESET_ALL + ' Delete person')

        print(Fore.MAGENTA + 'add_assignment.' + Style.RESET_ALL + ' Create assignment')

        print(
            Fore.GREEN + 'filter_by_description.' + Style.RESET_ALL + ' Show tasks which fit a given description')
        print(Fore.GREEN + 'by_date_report.' + Style.RESET_ALL + ' Show report of tasks by date')

        # reports - TO DO
        print(
            Fore.CYAN + 'print_busiest.' + Style.RESET_ALL + ' Print the first N persons in order of assigned tasks.')

        # search - TO DO

        print(
            Fore.CYAN + 'search_tasks.' + Style.RESET_ALL + ' Search tasks by given fields (e.g. status=pending, status = pending day=13, day=13')
        print(Fore.BLUE + 'print_tasks.' + Style.RESET_ALL + ' Print all tasks')
        print(Fore.BLUE + 'print_persons.' + Style.RESET_ALL + ' Print all persons')
        print(Fore.BLUE + 'print_assignments.' + Style.RESET_ALL + ' Print all assignments')

        print(Fore.RED + 'exit.' + Style.RESET_ALL + ' Exit')

    def print_entity_list(self, entity_list):
        for entity in entity_list:
            print(entity)

    def delete_task_ui(self):
        try:
            id = int(input("Please provide the id of the person you want to delete."))
            deleted_task = self.__task_service.delete_task(id)
            print(Fore.GREEN + "SUCCESS. " + Style.RESET_ALL)
            print('The task', str(deleted_task), 'was successfully deleted.')

        except ValueError:
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + "ID should be a number...")
        except RepositoryException as e:
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + str(e))

    def add_task_ui(self):
        id = input("Please provide ID:")
        description = input("Please provide description")
        data = input("Please provide date (e.g. 12-09):")
        status = input("Please provide task status:")
        try:
            id = int(id)
            day, month = data.split('-')
            day = int(day)
            month = int(month)
            self.__task_service.add_task(id, description, day, month, status)
            print(Fore.GREEN + 'SUCCESS: ' + Style.RESET_ALL + 'The task was successfully added.')
        except ValueError:
            print(Fore.RED + 'ERROR: Id, day, month fields should be numbers' + Style.RESET_ALL)

        except RepositoryException as e:
            print(Fore.RED + 'ERROR:' + str(e) + Style.RESET_ALL)

    def filter_tasks_by_description_ui(self):
        description_substr = input('Please provide description you want to search by:')
        filtered_tasks = self.__task_service.filter_by_description(description_substr)

        if len(filtered_tasks) > 0:
            print('These are the tasks that meet the criteria.')
            self.print_entity_list(filtered_tasks)
        else:
            print(Fore.MAGENTA + "No tasks fit the criteria." + Style.RESET_ALL)

    def show_task_report_ui(self):
        report = self.__task_service.get_report_by_day()
        # report is a dict
        for day, tasks in report.items():
            print('Day:', day)
            self.print_entity_list(tasks)

    def add_person_ui(self):
        print('Please provide person information:')
        cnp = input('CNP:')
        nume = input('Name:')
        try:
            self.__person_service.add_person(cnp, nume)
            print(Fore.GREEN + 'SUCCESS: ' + Style.RESET_ALL + 'Successfully added the person')
        except Exception as e:
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + str(e))

    def delete_person_ui(self):
        print('Please provide the CNP of the person you want to delete.')
        cnp = input('CNP:')
        try:
            self.__person_service.delete_person(cnp)
            print(Fore.GREEN + 'SUCCESS: ' + Style.RESET_ALL + 'Successfully deleted person.')
        except Exception as e:
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + str(e))

    def add_assignment_ui(self):
        id_assignment = input('Provide an id for the assignment:')
        id_task = input("Please provide task ID:")
        cnp_persoana = input("Please provide CNP of person:")
        evaluare = input("Please provide an evaluation of how fun the task was:")

        try:
            id_assignment = int(id_assignment)
            id_task = int(id_task)
            evaluare = float(evaluare)
            self.__assignment_service.create_assignment(id_assignment, id_task, cnp_persoana, evaluare)
        except Exception as e:
            print(Fore.RED + "ERROR: " + Style.RESET_ALL + str(e))

    def run(self):
        self._print_available_commands()
        while True:
            option = input('>').lower().strip()
            if option == 'help':
                self._print_available_commands()
            if option == "print_tasks":
                self.print_entity_list(self.__task_service.get_all_tasks())
            elif option == 'print_persons':
                self.print_entity_list(self.__person_service.get_all_persons())
            elif option == 'print_assignments':
                self.print_entity_list(self.__assignment_service.get_all())

            elif option == 'add_task':
                self.add_task_ui()
            elif option == 'del_task':
                self.delete_task_ui()


            elif option == 'add_person':
                self.add_person_ui()
            elif option == 'del_person':
                self.delete_person_ui()

            elif option == 'add_assignment':
                self.add_assignment_ui()

            elif 'search_tasks' in option:
                print('Searching for tasks:...')
                cmd_params = option.replace('search_tasks', '')
                self.search_for_tasks(cmd_params)
            elif option == 'filter_by_description':
                self.filter_tasks_by_description_ui()
            elif option == 'by_date_report':
                self.show_task_report_ui()


            elif option == "exit":
                break
            else:
                print("Invalid option.")

    def search_for_tasks(self, cmd_params):
        cmd_params = cmd_params.split()
        print(cmd_params)
        for element in cmd_params:
            criteria, value = element.split('=')
            print(criteria,value)
