from domain.task import Task
from domain.validator import TaskValidator


def test_create_task():
    task = Task(1,'BookSkydivingAdventure', 11, 12, 'pending')
    assert (task.get_descriere() == 'BookSkydivingAdventure')
    assert (task.get_zi_deadline() == 11)
    assert (task.get_luna_deadline() == 12)
    assert (task.get_status() == 'pending')
    task.set_descriere("ABC")
    assert (task.get_descriere() == 'ABC')
    assert (task.get_date() == '11/12')


def test_equal_tasks():
    task1 = Task(1, 'BookSkydivingAdventure', 11, 12, 'pending')
    task2 = Task(1, 'BookSkydivingAdventure', 11, 12, 'pending')
    assert (task1 == task2)

    task1 = Task(3, 'BookSkydivingAdventure', 12, 12, 'pending')
    task2 = Task(4, 'BookSkydivingAdventure', 12, 12, 'pending')
    assert (task1 != task2)


def test_validate_task():
    validator = TaskValidator()

    task1 = Task(1,"Host Movie Marathon", 10, 9, 'pending')
    try:
        validator.validate_task(task1)
        assert True
    except ValueError:
        assert False

    task2 = Task(2,"H", 10, 9, 'pending')
    try:
        validator.validate_task(task2)
        assert False
    except ValueError:
        assert True

    task3 = Task(1,"Movie Marathon", 56, 8, 'pending')
    try:
        validator.validate_task(task3)
        assert False
    except ValueError:
        assert True

    task4 = Task(1,"Host movie marathon", 10, 91, 'pending')
    try:
        validator.validate_task(task4)
        assert False
    except ValueError:
        assert True

    task5 = Task(1,"Host movie marathon", 10, 9, 'something')
    try:
        validator.validate_task(task5)
        assert False
    except ValueError:
        assert True
