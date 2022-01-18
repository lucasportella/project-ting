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
