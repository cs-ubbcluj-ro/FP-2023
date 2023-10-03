from archive.src_2022_2023.seminar.group_911.seminar_11.domain.exceptions import CarValidationException


class CarValidatorRO:
    @staticmethod
    def _is_license_valid(license):
        # TODO Implement full validation
        """
        Implement Romanian license plate validation
        @param license:
        @return: ...
        """
        return len(license) > 2

    # FIXME Duplicated code across validators, use inheritance to remove it
    def validate(self, car):
        errors = []
        # V1 - All properties are non-empty
        if not CarValidatorRO._is_license_valid(car.license_plate):
            errors.append('Invalid license plate')
        if len(car.make) < 2:
            errors.append('Car make should have at least 3 letters')
        if len(car.model) < 2:
            errors.append('Car model should have at least 3 letters')

        if len(errors) > 0:
            raise CarValidationException(errors)
