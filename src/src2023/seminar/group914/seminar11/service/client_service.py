from src2023.seminar.group914.seminar11.domain.client import Client
from src2023.seminar.group914.seminar11.service.undo_service import FunctionCall, Operation


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

    def delete(self, client_id):
        """
            1. Delete the client
        """
        client = self._repository.delete(client_id)

        """
        Record client deletion for undo/redo
        undo/redo do not have to be validated
        do not record undo/redo if the operation was not completed (exceptions)
        """
        redo_fun = FunctionCall(self._repository.delete, client_id)
        undo_fun = FunctionCall(self._repository.store, client)
        self._undo_service.record_undo(Operation(undo_fun, redo_fun))

        '''
            2. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        # TODO Also undo/redo the rentals
        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.getId(), False)

        return client

    def get_client_count(self):
        return len(self._repository)

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        pass
