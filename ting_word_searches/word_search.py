from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def exists_word(word, instance):
    return instance.exists_word(word)


def search_by_word(word, instance):
    return instance.search_by_word(word)


if __name__ == "__main__":
    # project = Queue()
    # process("statics/nome_pedro.txt", project)
    # word = exists_word("Pedro", project)

    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = search_by_word("pedro", project)
    print(word)
