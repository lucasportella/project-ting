class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def search(self, index):
        if index < 0 or index > len(self.data) - 1:
            raise IndexError("Invalid Index")
        return self.data[index]
