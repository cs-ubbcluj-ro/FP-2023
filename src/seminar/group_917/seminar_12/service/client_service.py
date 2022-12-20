from seminar.group_917.seminar_12.domain.client import Client
from seminar.group_917.seminar_12.service.undo_service import fun_call, operation, cascade_operation


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

        # Record for undo/redo
        undo_call = fun_call(self.create, client.id, client.cnp, client.name)
        redo_call = fun_call(self.delete, client.id)
        # self._undo_service.record_for_undo(operation(undo_call, redo_call))
        client_op = operation(undo_call, redo_call)

        '''
            2. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        # NOTE Handle later using cascading
        rental_op = []

        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.getId(), False)
            # undo_call = ...
            # redo_call = ...
            rental_op.append(operation(undo_call, redo_call))

        self._undo_service.record_for_undo(cascade_operation(client_op, *rental_op))
        return client

    def get_client_count(self):
        return len(self._repository)

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        pass
