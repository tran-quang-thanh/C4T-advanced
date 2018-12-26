class Queue:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
    def is_empty(self):
        return not bool(self.items)
    def insert(self, x):
        self.items.insert(0, x)
    def remove(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return 0
    def clear(self):
        self.items = []
    def __str__(self):
        return " ".join(str(i) for i in self.items)
    def size(self):
        return len(self.items)
    def is_full(self):
        return self.size() >= self.capacity
    def append(self, x):
        self.items.append(x)

# from stack import Stack
# class Queue:
#     def __init__(self):
#         self.items = Stack()
#         self.newItems = Stack()
#     def insert(self, addItem):
#         if self.items.is_empty():
#             self.items.push(addItem)
#         else:
#             while(not self.items.is_empty()):
#                 self.newItems.push(self.items.pop())
#             self.newItems.push(addItem)
#             while not self.newItems.is_empty():
#                 self.items.push(self.newItems.pop())
#     def is_empty(self):
#         return self.items.is_empty()
#     def remove(self):
#         return self.items.pop()
#     def __str__(self):
#         return self.items.__str__()
