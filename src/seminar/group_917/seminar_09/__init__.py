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
week 7 -> Tic Tac Toe with modular programming
week 8 -> Tic Tac Toe with classes and objects
week 9 -> classes and objects
    -> Write domain classes using properties
    -> Define our own exception classes
    -> Intro to Repository class and layer
    -> Working with text and binary files
    -> Intro to inheritance using Exceptions and Repositories
"""
