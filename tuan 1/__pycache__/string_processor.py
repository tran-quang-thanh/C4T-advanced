from stack import Stack

class StringProcessor:
    def __init__(self):
        self.stack = Stack()
    def reverse(self, new_str):
        self.stack.clear()
        for s in new_str:
            self.stack.push(s)
        new = ""
        for i in range(len(new_str)):
            new += self.stack.pop()
        return new
    def process_sequence(self, new_str):
        self.stack.clear()
        new = ""
        for i in new_str:
            if i != "*":
                self.stack.push(i)
            else:
                new += self.stack.pop()
        return new
    def binary_string(self, num):
        self.stack.clear()
        binary = ""
        if num == 0:
            binary = "0"
        else:
            while num > 0:
                self.stack.push(num % 2)
                num //= 2
            while (not self.stack.is_empty()):
                binary += str(self.stack.pop())
        return str(binary)
    def is_balanced(self, string):
        self.stack.clear()
        for s in string:
            if s == "{" or s == "[" or s == "(":
                self.stack.push(s)
            elif s == "}" and self.stack.pop() != "{":
                return False
            elif s == "]" and self.stack.pop() != "[":
                return False
            elif s == ")" and self.stack.pop() != "(":
                return False
        if not self.stack.is_empty():
            return False
        return True


