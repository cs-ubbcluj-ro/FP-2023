def print_repos_with_message(msg, client_repo, car_repo, rent_repo):
    print("-" * 15 + msg + "-" * 15)
    if client_repo is not None:
        print("Clients:\n" + str(client_repo))
    if car_repo is not None:
        print("Cars:\n" + str(car_repo))
    if rent_repo is not None:
        print("Rentals:\n" + str(rent_repo))
