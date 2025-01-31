import sys


def txt_importer(path_file):
    file_extension = path_file.split(".")[-1]
    if file_extension != "txt":
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, mode="rt") as file:
            content = file.read()
            return content.split("\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
