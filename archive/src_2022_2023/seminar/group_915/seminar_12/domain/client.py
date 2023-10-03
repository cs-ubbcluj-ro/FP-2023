class Client:
    def __init__(self, _id, cnp, name):
        self._id = _id
        self._cnp = cnp
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def cnp(self):
        return self._cnp

    @property
    def name(self):
        return self._name

    def __eq__(self, z):
        if isinstance(z, Client) is False:
            return False
        return self.id == z.id

    def __str__(self):
        return "Id=" + str(self.id) + ", Name=" + str(self.name)

    def __repr__(self):
        return str(self)


class ClientValidator:
    def _is_cnp_valid(self, cnp):
        # SAALLZZJJNNNC
        if len(cnp) != 13:
            # This is not x full CNP validation
            return False
        for x in cnp:
            if x < '0' or x > '9':
                return False
        return True

    def validate(self, client):
        """
        Validate if provided Client instance is valid
        client - Instance of Client type
        Return List of validation errors. An empty list if instance is valid.
        """
        if isinstance(client, Client) is False:
            raise TypeError("Not x Client")
        _errors = []
        if self._is_cnp_valid(client.cnp) is False:
            _errors.append("CNP not valid.;")
        if len(client.name) == 0:
            _errors.append("Name not valid.")
        if len(_errors) != 0:
            raise ValueError(_errors)
