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
1. Write a Car class so that:
    - it has fields for license plate, make, model and color (all are str)
    - class has properties for all fields
    - all properties are set in the class constructor (__init__)
    - property for license plates is read-only
    - remaining properties are read/write
    - override __str__ so cars are displayed nicely on console :)
    
2. Write a function that generates n cars (n - input parameter)
    - make sure license plates are Ro, make, model color are real
        (e.g., -> CJ 01 ABC, VW Polo, red)
    - have lists of counties, makes, models, colors and randomly pick :)
    
3. Write a CarRepo class:
    - keeps a list or dict of cars (protected field -> _data)
    - methods to add a car, delete a car, get a car by license plate, get all cars
    - override __len__ to return how many cars are in the repo
    - define a RepoException class that inherits from Exception
    - RepoException is in the same module as CarRepo
    - raise RepoException when:
        -> trying to add a car with existing license plates in repo
        -> calling get on a car that's not in the repo
    - NB! -> make the CarRepo iterable -> __iter__, __next__ ?
    
4. Write CarRepoTextFile class:
    - CarRepoTextFile is derived from CarRepo class
    - it adds a _load_file and a _save_file method
    - cars are kept in a CSV file (CSV - comma separated values)
    - cars are loaded from file when the constructor is called
    - cars are saved after every operation
"""

# _load_file
# r - read, t - text
fin = open(file_name, "rt")
# read all the lines in the file into a list
# each car should be represented on its own line
list_of_lines = fin.readlines()
# split lines by "," -> add them to repo

# _save_file
fout = open(file_name, "wt")
# turn each Car object into a one-line string -> CJ 01 ABC, Toyota, Yaris, red
# in a for loop :)
fout.write(car_as_string)
fout.close()
