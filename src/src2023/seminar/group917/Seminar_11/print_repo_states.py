def print_repo_contents(message, person_repository, task_repository, assignment_repository):
    print('-' * 10 + message + '-' * 10)
    if person_repository is not None:
        print('Current persons in repo are:')
        print(str(person_repository))
    
    if task_repository is not None:
        print('Current tasks in repo are:')
        print(str(task_repository))
    
    if assignment_repository is not None:
        print('Current assignments in repo are:')
        print(str(assignment_repository))
