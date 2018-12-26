class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return not bool(self.items)
    def push(self, num):
        self.items.append(num)
    def pop(self):
        return self.items.pop()
    def __str__(self):
        return " ".join(str(i) for i in self.items)
    def clear(self):
        self.items = []
