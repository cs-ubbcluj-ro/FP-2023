from domain.task import Task
from repository.memory_repository import TaskInMemoryRepository


def test_add_repo():
    test_repo = TaskInMemoryRepository()
    assert (test_repo.size() == 0)

    task = Task(1, "Join a book club", 11, 12, 'pending')
    test_repo.store(task)
    assert (test_repo.size() == 1)

    try:
        test_repo.store(task)
        assert False
    except ValueError:
        assert True

    task2 = Task(2, "Watch a Christmas movie", 27, 12, 'pending')
    test_repo.store(task2)
    assert (test_repo.size() == 2)


def test_find_repo():
    test_repo = TaskInMemoryRepository()
    assert (test_repo.size() == 0)

    task1 = Task(1, "Join a book club", 11, 12, 'pending')
    task2 = Task(2, "Watch a Christmas movie", 27, 12, 'pending')
    task3 = Task(3, "Make gingerbread", 20, 12, 'in-progress')

    test_repo.store(task1)
    test_repo.store(task2)
    test_repo.store(task3)

    assert (test_repo.size() == 3)

    assert (test_repo.find(1) is not None)
    assert (test_repo.find(2) is not None)
    assert (test_repo.find(3) is not None)
    assert (test_repo.find(10) is None)


def test_delete_repo():
    test_repo = TaskInMemoryRepository()
    task1 = Task(1, "Join a book club", 11, 12, 'pending')
    task2 = Task(2, "Watch a Christmas movie", 27, 12, 'pending')
    task3 = Task(3, "Make gingerbread", 20, 12, 'in-progress')

    test_repo.store(task1)
    test_repo.store(task2)
    test_repo.store(task3)
    assert (test_repo.size() == 3)

    deleted_task = test_repo.delete(1)
    assert (test_repo.size() == 2)
    assert (test_repo.find(1) is None)
    assert (deleted_task.get_descriere() == "Join a book club")

    deleted_task = test_repo.delete(3)
    assert (test_repo.size() == 1)
    assert (not test_repo.find(3))
    assert (deleted_task.get_descriere() == "Make gingerbread")

    test_repo.store(Task(1, "Take a break", 20, 11, 'done'))
    assert (test_repo.size() == 2)

    deleted_task = test_repo.delete(1)
    assert (test_repo.size() == 1)
    assert (test_repo.find(1) is None)
    assert (deleted_task.get_descriere() == "Take a break")

    try:
        test_repo.delete(111)
        assert False
    except ValueError:
        assert True


def test_update():
    pass
