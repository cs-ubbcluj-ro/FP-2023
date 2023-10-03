from archive.src_2022_2023.lecture.live.lecture_09_10.repo.converters import Converter
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.file_repo import FileRepo
from archive.src_2022_2023.lecture.live.lecture_09_10.repo.mem_repo import RepositoryError


class TextFileRepo(FileRepo):
    def __init__(self, converter: Converter, file_name="file.txt"):
        self._file_name = file_name
        self._converter = converter
        super().__init__()

    def _save_file(self):
        fout = open(self._file_name, "wt")
        for idobj in self._data.values():
            fout.write(self._converter.to_str(idobj) + "\n")
        fout.close()

    def _load_file(self):
        try:
            fin = open(self._file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except FileNotFoundError:
            # option 1: behave like no input file is normal => empty repo
            # we eat the exception :)
            # pass
            # option 2: file must be present => program cannot make progress
            raise RepositoryError("Input file does not exit")
        except IOError:
            # NOTE FileNotFoundError is handled in the except block above here
            # NOTE IOError that are not FileNotFoundError are handled here
            pass

        # NOTE PyCharm highlights the lines variable below, as it is initially defined in the try ... except block.
        # In case an IOError that is NOT a FileNotFoundError is raised, the variable remains undefined :)
        for line in lines:
            self.add(self._converter.from_str(line))
