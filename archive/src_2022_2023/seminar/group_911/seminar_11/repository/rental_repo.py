from archive.src_2022_2023.seminar.group_911.seminar_11.repository.repository_exception import RepositoryException


class RentalRepository:
    # TODO Finish implementation
    def __init__(self):
        self._data = {}

    def add(self, rental):
        if rental.id in self._data.keys():
            raise RepositoryException("Duplicate Rental ID")
        self._data[rental.id] = rental

    def remove(self, rental_id):
        if rental_id in self._data.keys():
            del self.data[rental_id]
        else:
            raise RepositoryException("Rental was not found")

    def get_all(self):
        return list(self._data.values())
