class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1

    def reset(self):
        self.count = 0


c = Counter()
c.tick()
print(c.count)
