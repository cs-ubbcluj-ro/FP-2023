from seminar.group_912.seminar_11.domain.car_validators import CarValidatorRO


class CarService:
    def __init__(self, repo, validator: CarValidatorRO):
        self._repo = repo
        self._validator = validator

    def get(self, car_id):
        return self._repo.get(car_id)

    # NOTE convenience for rental repo
    def get_all(self):
        return self._repo.get_all()
