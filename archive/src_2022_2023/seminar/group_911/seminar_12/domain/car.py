from archive.src_2022_2023.seminar.group_911.seminar_12.domain.validator_exception import ValidatorException


class Car:
    def __init__(self, _id, license_plate, make, model):
        self._id = _id
        self._license = license_plate
        self._make = make
        self._model = model

    @property
    def id(self):
        return self._id

    @property
    def license(self):
        return self._license

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    def __eq__(self, z):
        if not isinstance(z, Car):
            return False
        return self.id == z.id

    def __str__(self):
        return "Id: " + str(self.id) + ", License: " + self.license + ", Car type: " + self.make + ", " + self.model

    def __repr__(self):
        return str(self)


class CarValidator:

    def __init__(self):
        # and so on...
        self.__counties = ["AB", "B", "CJ"]
        self._errors = ""

    def _license_valid(self, plate):
        token = str(plate).split(' ')
        if len(token) != 3:
            return False
        if token[0] not in self.__counties:
            return False
        try:
            n = int(token[1])
            if len(token[1]) < 2 or len(token[1]) > 3:
                return False
            if n < 1 or n > 999:
                return False
            if n > 99 and token[0] != "B":
                return False
        except TypeError:
            return False
        if len(token[2]) != 3:
            return False
        tu = str(token[2]).upper()
        if tu[0] in ['I', 'O']:
            return False
        for x in tu:
            if x < 'A' or x > 'Z':
                return False
            if x == 'Q':
                return False
        return True

    def validate(self, car):
        """
        Validate if provided Car instance is valid
        car - Instance of Car type
        Return List of validation errors. An empty list if instance is valid.
        """
        if isinstance(car, Car) == False:
            raise TypeError("Can only validate Car objects!")
        _errors = []
        if len(car.make) == 0:
            _errors.append("Car must have x make")
        if len(car.model) == 0:
            _errors.append("Car must have x model;")
        if self._license_valid(car.license) is False:
            _errors.append("Bad license plate number;")
        if len(_errors) > 0:
            raise ValidatorException(_errors)
        return True
