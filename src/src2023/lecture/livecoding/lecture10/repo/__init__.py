"""
V1
    program.py --- the whole program was here

V2
    ui.py --- all user interaction (print/input)
    functions.py -- functions that talk via parameters/return

    ui.py -> functions.py

V3 (with classes and objects)
    ui (package)
        ui.py
    services (package)
        car_services.py
        client_services.py
        rental_services.py
    repository (package)
        repository.py --- more entities, more classes?
    domain (package)
        car.py
        client.py
        rental.py

Functionalities:
    1. add a new car
        a. read car data in the ui
        b. ui calls car_services.add_car( <new_car> )
        c. car_services.py validates the car (car_validator.py)
            -> car not valid => raise Exception,
            otherwise:
        d. car_services.py calls repository.add_car( <new_car> )

    2. statistic: the list of the most rented cars (cars that have the most
    number of rental days), sorted desc by the number of rental days
        rental_services.py
            a. get the list of all cars
            b. get the list of rentals for each car
            c. get the total rental days for each car
            d. sort them desc (use a DTO - data transfer object)
            e. return the list to the UI



"""