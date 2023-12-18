from domain.person import Person
from repository.repo_exceptions import DuplicateCNPException, \
    PersonDoesNotExistException


class PersonInMemoryRepository:
    def __init__(self):
        self.__persons = {}

    def store(self, person: Person):
        """
        Add person
        :param person: person to add
        :type person: Person
        :raises: DuplicateIDException if person with same CNP exists
        """

        if person.cnp in self.__persons:
            raise DuplicateCNPException()
        self.__persons[person.cnp] = person

    def get(self, cnp: str):
        """
        Find person with the given CNP
        """
        if cnp in self.__persons:
            return self.__persons[cnp]
        raise PersonDoesNotExistException()

    def delete(self, cnp):
        """
        Remove person with given cnp
        """

        if cnp not in self.__persons:
            raise PersonDoesNotExistException()
        deleted_person = self.__persons[cnp]
        del self.__persons[cnp]
        return deleted_person

    def get_all(self):
        return list(self.__persons.values())

    @property
    def size(self):
        return len(self.get_all())

    def __str__(self):
        persons_str = ""
        for person in self.__persons.values():
            persons_str += str(person) + '\n'

        return persons_str


class PersonFileRepository(PersonInMemoryRepository):
    def __init__(self, filename):
        PersonInMemoryRepository.__init__(self)
        self.__filename = filename
        self._load_from_file()

    def _load_from_file(self):
        """
        Load data from file
        """
        with open(self.__filename, mode='r', encoding='utf-8') as persons_file:
            lines = persons_file.readlines()
            lines = [line.strip() for line in lines if line.strip() != '']
            for line in lines:
                cnp, nume = line.split(',')
                cnp = cnp.strip()
                nume = nume.strip()
                PersonInMemoryRepository.store(self, Person(cnp, nume))

    def store(self, person: Person):
        """
        Add person
        :raises: DuplicateIDException if person with given CNP already exists
        """
        PersonInMemoryRepository.store(self, person)
        self._write_to_file()

    def delete(self, cnp):
        """
        Delete person with given CNP

        :raises: NonexistentIDException if person with given CNP does not exists
        """
        deleted_person = PersonInMemoryRepository.delete(self, cnp)
        self._write_to_file()
        return deleted_person

    def _write_to_file(self):
        """
        Write data to file
        """
        persons = PersonInMemoryRepository.get_all(self)
        persons = [person.cnp + ',' + person.name for person in persons]
        with open(self.__filename, mode='w', encoding='utf-8') as persons_file:
            text_to_write = '\n'.join(persons)
            persons_file.write(text_to_write)
