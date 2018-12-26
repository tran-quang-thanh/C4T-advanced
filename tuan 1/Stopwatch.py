class StopWatch:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
        if self.minute == 60:
            self.hour += 1
            self.minute = 0

    def reset(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def __str__(self):
        return "{0}h:{1}m:{2}s".format(self.hour, self.minute, self.second)

if __name__ == "__main__":
    c = StopWatch()
