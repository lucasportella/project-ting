from ting_file_management.file_management import txt_importer
import sys
from ting_file_management.queue import Queue


def process(path_file, instance):
    if instance.search_by_file(path_file):
        file_lines = txt_importer(path_file)
        lines_quant = len(file_lines)
        file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": lines_quant,
            "linhas_do_arquivo": file_lines,
        }
        instance.enqueue(file)
        sys.stdout.write(str(file))


def remove(instance):
    if len(instance) > 0:
        removed = instance.dequeue()
        sys.stdout.write(
            f'Arquivo {removed["nome_do_arquivo"]} removido com sucesso\n'
        )
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        sys.stdout.write(str(file))
    except IndexError:
        sys.stderr.write("Posição inválida")


if __name__ == "__main__":
    project = Queue()
    process("statics/novo_paradigma_globalizado-min.txt", project)
    file_metadata(project, 0)
