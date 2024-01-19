class IdGenerator:
    def __init__(self, gen_file="last_id.txt"):
        self.__gen_file = gen_file
        self.__last_id = self.__load_last_id()

    def generate_id(self):
        self.__last_id += 1
        self.__save_last_id()
        return self.__last_id

    def __load_last_id(self):
        try:
            with open(self.__gen_file, "r") as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def __save_last_id(self):
        with open(self.__gen_file, "w") as f:
            f.write(str(self.__last_id))
