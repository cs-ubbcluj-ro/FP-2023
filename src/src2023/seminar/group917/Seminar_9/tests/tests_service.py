from domain.validator import TaskValidator
from repository.memory_repository import TaskInMemoryRepository
from service.service import TaskController


def test_add_service():
    repo = TaskInMemoryRepository()
    validator = TaskValidator()
    task_service = TaskController(repo, validator)
    task_service.add_task(1, 'HostMovieMarathon', 10, 8, 'pending')
    test_task_list = task_service.get_all_tasks()
    assert (len(test_task_list) == 1)

    try:
        task_service.add_task(1, "Valid task Duplicate ID", 10, 5, 'pending')
        assert False
    except ValueError:
        assert True

    try:
        task_service.add_task(2, "Invalid task ID ok", 1001, 500, 'done')
        assert False
    except ValueError:
        assert True


def test_search_by_date():
    repo = TaskInMemoryRepository()
    validator = TaskValidator()
    task_service = TaskController(repo, validator)

    assert (task_service.filter_by_date(5, 5, 10, 8) == [])

    task_service.add_task(1, 'HostMovieMarathon', 10, 8, 'pending')
    task_service.add_task(2, 'Read Book', 5, 3, 'pending')
    task_service.add_task(3, 'Build Treehouse', 1, 10, 'pending')

    assert (len(task_service.filter_by_date(5, 5, 6, 11)) == 2)

    task_service.add_task(4, 'HostMovieMarathon', 5, 8, 'pending')

    assert (len(task_service.filter_by_date(5, 5, 6, 11)) == 3)

    task_service.add_task(5, 'HostMovieMarathon', 1, 11, 'pending')

    assert (len(task_service.filter_by_date(5, 5, 6, 11)) == 4)
    assert (len(task_service.filter_by_date(5, 5, 1, 11)) == 4)


def test_filter_by_description():
    repo = TaskInMemoryRepository()
    task_validator = TaskValidator()
    task_service = TaskController(repo, task_validator)
    task_service.add_task(1, "Travel to see Grand Canyon", 11, 9, 'pending')
    task_service.add_task(2, "Travel abroad", 10, 5, 'pending')
    task_service.add_task(3, "Try new banana bread recipe", 11, 2, "done")
    task_service.add_task(4, "Host a Halloween party", 31, 10, 'in-progress')
    task_service.add_task(5, "Buy stuff for New Year party", 28, 12, "pending")

    filtered_by_travel = task_service.filter_by_description('travel')
    assert (len(filtered_by_travel) == 2)
    assert (len(task_service.get_all_tasks()) == 5)

    filtered_by_recipe = task_service.filter_by_description('recipe')
    assert (len(filtered_by_recipe) == 1)
    assert (len(task_service.get_all_tasks()) == 5)

    filtered_by_cook = task_service.filter_by_description('cook')
    assert (len(filtered_by_cook) == 0)
    assert (len(task_service.get_all_tasks()) == 5)


def test_delete_by_status():
    repo = TaskInMemoryRepository()
    task_validator = TaskValidator()
    task_service = TaskController(repo, task_validator)

    task_service.delete_by_status('pending')
    assert (len(task_service.get_all_tasks()) == 0)

    task_service.add_default_tasks()
    # Initial: pending - 3, in-progress - 2, done - 5

    task_service.delete_by_status('pending')
    assert (len(task_service.get_all_tasks()) == 7)

    task_service.delete_by_status('in-progress')
    assert (len(task_service.get_all_tasks()) == 5)

    task_service.delete_by_status('done')
    for task in task_service.get_all_tasks():
        print(task)
    assert (len(task_service.get_all_tasks()) == 0)


def test_delete_by_id():
    repo = TaskInMemoryRepository()
    task_validator = TaskValidator()
    task_service = TaskController(repo, task_validator)

    task_service.add_task(1, "Travel to see Grand Canyon", 11, 9, 'pending')
    task_service.add_task(2, "Travel abroad", 10, 5, 'pending')
    task_service.add_task(3, "Try new banana bread recipe", 11, 2, "done")

    task_service.delete_task(1)
    assert (len(task_service.get_all_tasks()) == 2)

    try:
        task_service.delete_task(102)
        assert False
    except ValueError:
        assert True

    task_service.delete_task(2)
    assert (len(task_service.get_all_tasks()) == 1)
    task_service.delete_task(3)
    assert (len(task_service.get_all_tasks()) == 0)

    try:
        task_service.delete_task(3)
        assert False
    except ValueError:
        assert True

def test_get_report_by_day():
    repo = TaskInMemoryRepository()
    task_validator = TaskValidator()
    task_service = TaskController(repo, task_validator)

    report_dict = task_service.get_report_by_day()
    assert (len(report_dict.keys()) == 0)
    # also works with assert (not report_dict)
    task_service.add_default_tasks()

    report_dict = task_service.get_report_by_day()
    assert (len(report_dict['4/4']) == 1)

    assert (len(report_dict['5/8']) == 2)

    assert (len(report_dict['12/9']) == 3)

    try:
        number_of_tasks = len(report_dict['1-1'])
        assert False
    except KeyError:
        assert True
