from datetime import date

from archive.src_2022_2023.seminar.group_911.seminar_12.domain.car import CarValidator
from archive.src_2022_2023.seminar.group_911.seminar_12.domain.client import ClientValidator
from archive.src_2022_2023.seminar.group_911.seminar_12.domain.rental import RentalValidator
from archive.src_2022_2023.seminar.group_911.seminar_12.repository.repository import Repository
from archive.src_2022_2023.seminar.group_911.seminar_12.service.car_service import CarService
from archive.src_2022_2023.seminar.group_911.seminar_12.service.client_service import ClientService
from archive.src_2022_2023.seminar.group_911.seminar_12.service.rental_service import RentalService
from archive.src_2022_2023.seminar.group_911.seminar_12.service.undo_service import UndoService
from archive.src_2022_2023.seminar.group_911.seminar_12.util import print_repos_with_message


def undo_example_hardest():
    """
    An example for doing multiple undo operations. 
    This is a bit more difficult due to the fact that there are now several controllers,
    and each of them can perform operations that require undo support.
     
    Follow the code below and figure out how it works!
    """
    undo_service = UndoService()
    client_repo = Repository()
    car_repo = Repository()

    '''
    Start rental Service
    '''
    rent_repo = Repository()
    rent_validator = RentalValidator()
    rent_service = RentalService(undo_service, rent_validator, rent_repo, car_repo, client_repo)

    '''
    Start client Service
    '''
    client_validator = ClientValidator()
    client_service = ClientService(undo_service, rent_service, client_validator, client_repo)

    '''
    Start car Service
    '''
    car_validator = CarValidator()
    car_service = CarService(undo_service, rent_service, car_validator, car_repo)

    '''
    We add 1 client, 1 car and 2 rentals
    '''
    sophia = client_service.create(103, "2990511035588", "Sophia")
    hyundai_tucson = car_service.create(201, "CJ 02 TWD", "Hyundai", "Tucson")
    rent_service.create_rental(301, sophia, hyundai_tucson, date(2016, 11, 1), date(2016, 11, 30))
    rent_service.create_rental(302, sophia, hyundai_tucson, date(2016, 12, 1), date(2016, 12, 31))

    print_repos_with_message("We added Sophia, the Hyundai and its 2 rentals", client_repo, car_repo, rent_repo)

    car_service.delete(201)
    print_repos_with_message("Delete the Hyundai (also deletes its rentals)", client_repo, car_repo, rent_repo)

    '''
    Now undo the performed operations, one by one
    '''
    undo_service.undo()
    print_repos_with_message("1 undo, the Hyundai and its rentals are back", client_repo, car_repo, rent_repo)

    undo_service.undo()
    print_repos_with_message("1 undo deletes the second rental", client_repo, car_repo, rent_repo)

    undo_service.undo()
    print_repos_with_message("1 undo deletes the first rental", client_repo, car_repo, rent_repo)

    undo_service.undo()
    print_repos_with_message("1 undo deletes the Hyundai", client_repo, car_repo, rent_repo)

    '''
    After 5 undos, all repos should be empty, as we did 5 operations in total
    '''
    undo_service.undo()
    print_repos_with_message("1 undo deletes Sophia (no more undos)", client_repo, car_repo, rent_repo)

    '''
    Redos start here
    '''
    undo_service.redo()
    print_repos_with_message("1 redo and Sophia is added", client_repo, car_repo, rent_repo)

    undo_service.redo()
    print_repos_with_message("1 redo adds the Hyundai", client_repo, car_repo, rent_repo)

    undo_service.redo()
    print_repos_with_message("1 redo adds the first rental", client_repo, car_repo, rent_repo)

    undo_service.redo()
    print_repos_with_message("1 redo adds the second rental", client_repo, car_repo, rent_repo)

    undo_service.redo()
    print_repos_with_message("1 redo deletes the Hyundai and its rentals (again)", client_repo, car_repo, rent_repo)

    '''
    Let's do a few undos again...
    '''
    undo_service.undo()
    undo_service.undo()
    undo_service.undo()

    print_repos_with_message("3 undos later, we have Sophia and the Hyundai", client_repo, car_repo, rent_repo)

    '''
    Now we try something new - let's add another car!
    
    NB!
        A new operation must invalidate the history for redo() operations
    '''
    car_service.create(202, "CJ 02 SSE", "Dacia", "Sandero")
    print("\n Do we have a redo? -", undo_service.redo(), "\n")

    '''
    Now we should have 2 cars
    '''
    print_repos_with_message("After adding the Dacia, there is no redo ", client_repo, car_repo, rent_repo)

    '''
    However, undos is still available !
    '''
    undo_service.undo()
    print_repos_with_message("1 undo deletes the Dacia", client_repo, car_repo, rent_repo)

    undo_service.undo()
    print_repos_with_message("1 undo deletes the Hyundai", client_repo, car_repo, rent_repo)


undo_example_hardest()
