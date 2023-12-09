# Extra-reading: dataclasses
from colorama import Fore, Style


class Task:

    def __init__(self, id, descriere, zi_deadline, luna_deadline, status):
        self.__id = id
        self.__descriere = descriere
        self.__zi_deadline = zi_deadline
        self.__luna_deadline = luna_deadline
        self.__status = status

    #Extra-reding: @property decorator
    def get_descriere(self):
        return self.__descriere

    def get_id(self):
        return self.__id

    def get_zi_deadline(self):
        return self.__zi_deadline

    def get_luna_deadline(self):
        return self.__luna_deadline

    def get_status(self):
        return self.__status

    def set_descriere(self, descriere_noua):
        self.__descriere = descriere_noua

    def set_zi(self, zi_noua):
        self.__zi_deadline = zi_noua

    def set_luna(self, luna_noua):
        self.__luna_deadline = luna_noua

    def set_status(self, status):
        self.__status = status

    def get_date(self):
        return str(self.__zi_deadline) + '/' + str(self.__luna_deadline)

    def __eq__(self, other):
        """
        Seminar 7: Definim egalitate pe baza de id
        """
        return self.__id == other.get_id()

    def __str__(self):
        return "ID: "+str(self.get_id())+" | " +Fore.GREEN + "Descriere: " + self.get_descriere() + Style.RESET_ALL + " | " + Fore.MAGENTA + "Zi deadline:" + str(
            self.get_zi_deadline()) + ' | Luna deadline: ' + str(
            self.get_luna_deadline()) + Style.RESET_ALL + ' | ' + Fore.BLUE + \
            'Status: ' + self.get_status() + Style.RESET_ALL

