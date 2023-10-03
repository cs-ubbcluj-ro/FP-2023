class CarService:
    def __init__(self, repo, car_validator):
        self._repo = repo
        self._validator = car_validator

    def get(self, car_id):
        return self._repo.get(car_id)

    def get_all(self):
        return self._repo.get_all()
