class Stack(object):
    """Stack class"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def add(self, entry):
        self.items.append(entry)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]
