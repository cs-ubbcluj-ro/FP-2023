"""
Process the settings.properties here
- read the settings file exactly once
- read the file exactly when it is (first) needed
- give the entire program access to it
"""


class Settings:
    """
    Settings implements the Singleton design pattern
    https://refactoring.guru/design-patterns/singleton

    Use get_instance() to return the single object

    When working in C++/Java/C#/...
        1. mark the class constructor as private
        2. make sure get_instance() cannot be called from more
        than 1 thread
    """
    def __init__(self, repo_type: str, repo_file: str):
        self.__repo_type = repo_type
        self.__repo_file = repo_file

    @property
    def repo_type(self):
        return self.__repo_type

    @property
    def repo_file(self):
        return self.__repo_file

    # NOTE field instance belongs to class Settings, and not
    # to any particular object
    __instance = None

    @staticmethod
    def __load():
        repo_type = None
        repo_file = None

        f = open("settings.properties", "rt")
        lines = f.readlines()
        f.close()
        for line in lines:
            tokens = line.split("=")
            if tokens[0].strip() == "type":
                repo_type = tokens[1].strip()
            if tokens[0].strip() == "file":
                repo_file = tokens[1].strip()

        if repo_type is None or repo_file is None:
            pass  # ?????

        return Settings(repo_type, repo_file)

    @staticmethod
    def get_instance():
        if Settings.__instance is None:
            # we initialize at first call
            # Lazy initialization
            Settings.__instance = Settings.__load()
        return Settings.__instance
