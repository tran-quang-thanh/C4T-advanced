from numpy import random

class Simulation:
    def __init__(self, process_rate, min_req_rate, max_req_rate):
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate
    def run(self, num):
        no_of_lost = 0
        total_req = 0
        for i in range(num):
            req_rate = random.randint(self.min_req_rate, self.max_req_rate + 1)
            if req_rate > self.process_rate:
                no_of_lost += (req_rate - self.process_rate)
        return no_of_lost / num
