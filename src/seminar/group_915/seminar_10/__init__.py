"""
Create an application for a car rental business using a console based user interface.
The application must allow keeping records of the company’s list of clients, existing car pool and rental history.
The application must allow its users to manage clients, cars and rentals in the following ways:
    Clients
         Add a new client. Each client is a physical person having a unique ID (driver license series), name, age.
         Update the data for any client.
         Remove a client from active clients. Note that removing a client must not remove existing car rental statistics.
         Search for clients based on ID and name [both at the same time]
         All client operations must undergo proper validation!
    Cars
         Add a new car to the car pool. Each car must have a valid license plate number, a make and model taken from a
        list of makes and models. In addition, each car will have a color.
         Remove a car from the car pool.
         Search for cars based on license number, make, model and color.
            [make = VW, model = Polo, CJ01ABC], [make = VW, model = Polo, CJ01XYZ]
         All car operations must undergo proper validation!
    Rentals
         An existing client can rent one or several cars from the car pool for a determined period. When rented, a car
        becomes unavailable for further renting.
         When a car is returned, it becomes available for renting once again.
         Search the rental history of a given client, car, or all rentals during any given period.
    Statistics
         The list of all cars in the car pool sorted by number of days they were rented.
         The list of clients sorted descending by the number of cars they have rented.

    The application must have support for unlimited undo/redo with cascading.
"""

"""
1. Write a Car class
    - have a constructor that takes as parameters the car's license plates,
    the make, the model and the color (all are str)
    -> CJ 01 ABC, Dacia, Logan, red (make: Dacia, model: Logan)
    - use properties (@property) to access all the fields (license plate, make, model, color)
    - license plates are read-only (don't provide a setter property)
    - override __str__ to pretty print the car :)
    
2. write a generate_cars(n : int) function
    - function should not be in any class 
    - function should return the list of 'n' generated cars
    - generated cars: license plates should be real (random pick between counties, 
    generate the number and letter combination part)
    - make, model and color should also be real (random.choice() in a predefined list)
    
3. Write the CarRepo class (this is a repository for cars)
    - has a protected list or dict where we store cars
    - has methods to add a car, to delete a car, to return all the cars
    - raises RepoException (you have to implement this class) when:
        -> trying to add a car with an existing license plate
        -> trying to get a car with a non-existing license plate
    - override __len__ to return the number of cars in the repo
    !! Make the repo iterable
            for car in car_repo:
                print(car)
            
4. Write the CarRepoTextFile class that extends the CarRepo class
    - CarRepoTextFile class inherits CarRepo class
    - it adds the _load_file and _save_file methods
        -> _load_file - loads text file of cars into repo
        -> _save_file - saves cars into the text file
"""


class Car:
    def __init__(self, license_plate: str, make: str, model: str, color: str):
        self.__license_plate = license_plate
        self.make = make
        self.model = model
        self.color = color

    @property
    def license_plate(self):
        return self.__license_plate

    @property
    def make(self):
        return self.__car_make

    @make.setter
    def make(self, new_make):
        self.__car_make = new_make

    @property
    def model(self):
        return self.__car_model

    @model.setter
    def model(self, new_car_model):
        self.__car_model = new_car_model

    @property
    def color(self):
        return self.__car_color

    @color.setter
    def color(self, new_car_color):
        self.__car_color = new_car_color

    def __repr__(self):
        """
        str representation of this object
        """
        return str(self)

    def __str__(self):
        return f'Car: {self.__license_plate}, {self.make}, {self.model}, {self.color}'


if __name__ == "__main__":
    car = Car("CJ 99 ERT", "Mazda", "CX-30", "blue")

    print(car)
    car.make = "Toyota"
    car.color = "white"
    print(car)
