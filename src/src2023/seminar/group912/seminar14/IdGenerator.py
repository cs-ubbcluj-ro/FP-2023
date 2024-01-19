class IdGenerator:

    def __init__(self, file_name="id_counter.txt"):
        self.__file_name = file_name
        self.__counter = None

    def __load_file(self):
        try:
            f = open(self.__file_name, "r")
        except FileNotFoundError:
            self.__counter = 0
            return

        # NOTE Things loaded from a file are presumed correct
        self.__counter = int(f.readline().strip())
        f.close()

    def __save_file(self):
        f = open(self.__file_name, "w")
        f.write(str(self.__counter))
        f.close()

    def get_next_id(self):
        if self.__counter is None:
            # NOTE Lazy loading from the file
            self.__load_file()
        self.__counter += 1
        self.__save_file()
        return self.__counter
