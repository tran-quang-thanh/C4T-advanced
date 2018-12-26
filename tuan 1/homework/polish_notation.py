from stack import Stack

class PolishNotation:
    def __init__(self):
        self.cal = Stack()
    def calculate(self, equation):
        num = 0
        for s in equation:
            if (s != "+" and s != "-" and s != "*" and s != "/"):
                self.cal.push(s)
            else:
                if s == "+":
                    last = (int)(self.cal.pop())
                    num = last + (int)(self.cal.pop())
                elif s == "-":
                    last = (int)(self.cal.pop())
                    num = (int)(self.cal.pop()) - last
                elif s == "*":
                    last = (int)(self.cal.pop())
                    num = (int)(self.cal.pop()) * last
                elif s == "/":
                    last = (int)(self.cal.pop())
                    num = (int)(self.cal.pop()) // last
                self.cal.push(num)
        return num