from colorama import Fore, Style


class Console:
    def __init__(self, controller):
        self.__task_service = controller

    def __print_menu(self):
        print("Optiuni meniu:")
        print('1. Adaugare task')
        print('2. Stergere task')

        # Functionalitati de filtrare, rapoarte
        print('5. [FILTRARE] Afisare task-uri carre contin in descriere string')
        print('6. [RAPORT] Afisare raport pe luna')

        # Functionalitati utile care nu apar in mod explicit in cerinta
        print('P. Afisarea tuturor task-urilor')
        print('A. Adaugare task-uri default')
        print('E. Iesire')

    def print_task_list(self, task_list):
        for task in task_list:
            print(task)

    def delete_by_id_ui(self):
        try:
            id = int(input("Introuduceti id dupa care se sterge:"))
            deleted_task = self.__task_service.delete_task(id)
            print(Fore.GREEN + "SUCCES: " + Style.RESET_ALL + 'Stergere efectuata cu succes:')
            print('Task-ul', str(deleted_task), 's-a sters cu succes.')

        except Exception as e:
            print(Fore.RED + "EROARE: " + Style.RESET_ALL + str(e))

    def add_task_ui(self):
        id = input("Introduceti id:")
        descriere = input("Introduceti descrierea:")
        data = input("Introduceti data:")
        status = input("Introduceti status:")
        try:
            id = int(id)
            zi, luna = data.split('-')
            zi = int(zi)
            luna = int(luna)
            self.__task_service.add_task(id, descriere, zi, luna, status)
            print(Fore.GREEN + 'SUCCES: ' + Style.RESET_ALL + 'Adaugarea fost efectuata cu succes.')

        except Exception as e:
            print(Fore.RED + 'EROARE:' + str(e) + Style.RESET_ALL)


    def filter_by_description_ui(self):
        descriere_substr = input('Introduceti parte din descriere:')
        filtered_tasks = self.__task_service.filter_by_description(descriere_substr)

        if len(filtered_tasks) > 0:
            print('Task-urile care contin in descriere textul dat sunt:')
            self.print_task_list(filtered_tasks)
        else:
            print(Fore.MAGENTA + "Nu exista task-uri pentru care descrierea contine string-ul dat." + Style.RESET_ALL)

    def show_report_ui(self):
        report = self.__task_service.get_report_by_day()
        # report is a dict
        for day, tasks in report.items():
            print('Ziua:', day)
            self.print_task_list(tasks)

    def add_default_tasks_ui(self):
        try:
            self.__task_service.add_default_tasks()
            print(
                Fore.GREEN + 'SUCCES: ' + Style.RESET_ALL + 'Adaugarea task-urilor default a fost efectuata cu succes.')
        except Exception:
            print(
                Fore.RED + 'ERROR: ' + Style.RESET_ALL + 'Adaugarea task-urilor default a esuat. Cel mai probabil au mai fost adaugate o data.')

    def run(self):

        while True:
            self.__print_menu()
            option = input('>')
            option = option.upper().strip()
            if option == "P":
                self.print_task_list(self.__task_service.get_all_tasks())
            elif option == 'A':
                self.add_default_tasks_ui()
            elif option == '1':
                self.add_task_ui()
            elif option == '2':
                self.delete_by_id_ui()
            elif option == '5':
                self.filter_by_description_ui()
            elif option == '6':
                self.show_report_ui()
            elif option == "E":
                break
            else:
                print("Invalid option.")
