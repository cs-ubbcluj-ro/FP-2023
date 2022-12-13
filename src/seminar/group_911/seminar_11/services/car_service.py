from seminar.group_911.seminar_11.domain.car import Car


class CarService:
    def __init__(self, repo, validator):
        # self._repo = CarRepo()
        # NOTE Taking parameters in ctor allows you to change them
        self._repo = repo
        self._validator = validator

    def add_car(self, car_id: str, car_make: str, car_model: str, color: str):
        """
        Add a new car
        """
        # 1. Build Car instance
        car = Car(car_id, car_make, car_model, color)
        # 2. Validate Car instance
        self._validator.validate(car)
        # 3. Add car to repo
        self._repo.add(car)

    def get_all(self):
        return self._repo.get_all()