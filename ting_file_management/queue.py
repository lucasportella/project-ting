class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError

    def peek(self):
        return self.data[-1]

    def search_by_file(self, path_file):
        for dict in self.data:
            if dict["nome_do_arquivo"] == path_file:
                return False
        return True

    def exists_word(self, word):
        result = []
        for dict in self.data:
            file_search = {
                "palavra": word,
                "arquivo": dict["nome_do_arquivo"],
                "ocorrencias": [],
            }
            for index, line in enumerate(dict["linhas_do_arquivo"]):
                if word in line:
                    file_search["ocorrencias"].append({"linha": index + 1})
            if len(file_search["ocorrencias"]) > 0:
                result.append(file_search)
        return result

    def search_by_word(self, word):
        lower_word = word.lower()
        result = []
        for dict in self.data:
            file_search = {
                "palavra": lower_word,
                "arquivo": dict["nome_do_arquivo"],
                "ocorrencias": [],
            }
            for index, line in enumerate(dict["linhas_do_arquivo"]):
                if lower_word in line.lower():
                    file_search["ocorrencias"].append(
                        {"linha": index + 1, "conteudo": line}
                    )
            if len(file_search["ocorrencias"]) > 0:
                result.append(file_search)
        return result
