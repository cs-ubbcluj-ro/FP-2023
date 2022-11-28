from ..domain.car import car


# RepoException inherits from Python's builtin Exception class
# RepoException "IS AN" exception
class RepoException(Exception):
    pass


class car_repo:
    pass


def test_car_repo():
    repo = car_repo()
    # car repository is empty
    assert len(repo) == 0

    # add cars to the repo
    c1 = car("CJ 01 ABC", "Dacia", "Sandero", "red")
    repo.add(c1)
    c2 = car("CJ 01 XYZ", "Dacia", "Logdy", "white")
    repo.add(c2)
    assert len(repo) == 2

    # try to add the same car again
    try:
        repo.add(c1)
        assert False
    except RepoException:
        assert True

    # retrieve cars from repo
    assert repo.get("CJ 01 ABC") == c1
    assert repo.get("CJ 01 XYZ") == c2

    # try to retrieve a non-existing car
    try:
        repo.get("SJ 04 RTY")
        assert False
    except RepoException:
        assert True
