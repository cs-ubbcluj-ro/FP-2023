from archive.src_2022_2023.seminar.group_915.seminar_12.domain.client import Client
from archive.src_2022_2023.seminar.group_915.seminar_12.service.undo_service import command, operation


class ClientService:
    def __init__(self, undo_service, rental_service, validator, repository):
        self._validator = validator
        self._repository = repository
        self._rental_service = rental_service
        self._undo_service = undo_service

    def create(self, client_id, client_cnp, client_name):
        client = Client(client_id, client_cnp, client_name)
        self._validator.validate(client)
        self._repository.store(client)
        return client

    def _delete_impl(self, client_id):
        """
        1. Delete the client
        """
        client = self._repository.delete(client_id)

        '''
        2. Delete their rentals
        NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.getId(), False)

        return client

    def delete(self, client_id):
        """
            1. Delete the client
        """
        client = self._delete_impl(client_id)

        # here we record client deletion for undo/redo purposes
        undo_call = command(self.create, client.id, client.cnp, client.name)
        redo_call = command(self._delete_impl, client.id)
        self._undo_service.record(operation(undo_call, redo_call))

        return client

    def get_client_count(self):
        return len(self._repository)

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        pass
