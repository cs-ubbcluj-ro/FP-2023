"""
https://refactoring.guru/design-patterns/singleton
"""


class IdGeneratorSingleton:
    _instance = None

    def __init__(self, filename):
        print("Init was called")
        self.__filename = filename

    def __new__(cls, filename):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __read_id_from_file(self):
        last_used_id = int(open(self.__filename, 'r').readline().strip())
        return last_used_id

    def __save_id_to_file(self, last_used_id):
        with open(self.__filename, 'w') as f:
            f.write(str(last_used_id))

    def generate_id(self):
        # Can also keep field __id
        last_used_id = self.__read_id_from_file()
        new_id = last_used_id + 1
        self.__save_id_to_file(new_id)
        return new_id

    # @staticmethod
    # def get_instance(self):
    #     if IdGeneratorSingleton._instance is None:
    #         IdGeneratorSingleton._instance = IdGeneratorSingleton()
    #     return IdGeneratorSingleton._instance


# Try to generate some IDs
# id_generator1 = IdGeneratorSingleton('last_used_id.txt')
# id1 = id_generator1.generate_id()
# print(f"ID 1: {id1}")
#
# id_generator2 = IdGeneratorSingleton('last_used_id.txt')
# id2 = id_generator2.generate_id()
# print(f"ID 2: {id2}")
#
# # Are id_generator1 and id_generator2 the same instance?
# print(id(id_generator1))
# print(id(id_generator2))
# print(f"Are id_generator1 and id_generator2 the same instance? {id_generator1 is id_generator2}")
