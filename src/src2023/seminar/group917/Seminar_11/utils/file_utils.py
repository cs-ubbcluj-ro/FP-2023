import shutil

def copy_file_content(source_file, destination_file):
    """
    Copiaza continutul fisierul sursa in fisierul destinatie
    :param source_file: numele (path-ul) fisierului sursa
    :type source_file: str
    :param destination_file: numele (path-ul) fisierului destinatie
    :type destination_file: str
    :return:
    :rtype:
    """
    shutil.copyfile(source_file, destination_file)


def clear_file_content(filename):
    """
    Sterge continutul fisierului cu numele filename
    :param filename: numele (path-ul) fisierului din care vrem sa stergem continutul
    :type filename: str
    :return:
    :rtype:
    """
    with open(filename,'w') as f:
        pass