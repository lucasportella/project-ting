from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(instance.__len__()):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return False

    text = txt_importer(path_file)
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text,
    }

    instance.enqueue(file_dict)
    print(file_dict, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    else:
        file_deleted = instance.dequeue()
        return sys.stdout.write(
            f"Arquivo {file_deleted['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        return print(instance.search(position), file=sys.stdout)
    except IndexError:
        return sys.stderr.write("Posição inválida")
