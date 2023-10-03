from archive.src_2022_2023.seminar.group_912.seminar_12.domain.client import Client
from archive.src_2022_2023.seminar.group_912.seminar_12.service.undo_service import call, operation, cascaded_operation


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

        undo = call(self.create, client.id, client.cnp, client.name)
        redo = call(self.delete, client.id)
        # self._undo_service.record(operation(undo, redo))
        # undo/redo for client
        undo_op = [operation(undo, redo)]

        '''
            2. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.getId(), False)
            undo_call = call(self._rental_service.create_rental, rent.id, rent.client, rent.car, rent.start, rent.end)
            redo_call = call(self._rental_service.delete_rental, rent.id)
            undo_op.append(operation(undo_call, redo_call))

        # record the cascaded operation for undo/redo
        self._undo_service.record(cascaded_operation(*undo_op))

        return client

    def get_client_count(self):
        return len(self._repository)

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        pass
