class UI:
    def __init__(self, car_service, rent_service, client_service):
        pass


"""
Layered architecture
    ui  -> user interface
        -> all print/input (or all GUI windows/dialogs/menus etc)
        -> in our case we catch exception and display them here
    services
        -> below the UI layer (UI calls functions in services)
        -> does not know about the UI
        -> forward calls to repo, implement functionalities (undo/redo, statistics, search, etc.)
    repository 
        -> stores everything (preferably using files/SQL/noSQL)
        -> does not know about UI, services
    domain
        -> classes that we find in the problem statement (cars, expense, client, student, book, etc.)
        -> does not know about any layer
        
    function call direction:
        ui -> services -> repository
        
Dependency injection
    -> e.g., services need a repo to work, but you can vary the repo implementation
    
    Statistics
     The list of all cars in the car pool sorted by number of days they 
    were rented.
     The list of clients sorted descending by the number of cars they have rented.
     
"""
