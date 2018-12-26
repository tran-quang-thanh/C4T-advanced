from queue import Queue
from numpy import random

class QueueSimulation:
    def __init__(self, process_rate, min_req_rate, max_req_rate, queue_capacity):
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate
        self.queue_capacity = queue_capacity
        self.queue = Queue(self.queue_capacity)
        self.queue_step = Queue(self.queue_capacity)
        self.result = []

    def run(self, iteration):
        no_of_lost = 0
        for i in range(iteration):
            req_rate = random.randint(self.min_req_rate, self.max_req_rate + 1)
            new_process = self.process_rate
            while not self.queue.is_empty():
                new_process -= self.queue.remove()
            if req_rate > new_process:
                while req_rate > new_process and not self.queue.is_full():
                    self.queue.insert(1)
                    req_rate -= 1
                if req_rate > new_process:
                    no_of_lost += (req_rate - new_process)
        return no_of_lost / iteration

    def step(self, list):
        lost_count = 0
        self.result = []
        check = []
        while not self.queue_step.is_empty():
            check.append(self.queue_step.remove())
        while len(check) > 0:
            self.result.append(check.pop())
        self.queue_step.clear()
        available = self.process_rate - len(self.result)
        for j in list:
            if available > 0:
                self.result.append(j)
                available -= 1
            else:
                if not self.queue_step.is_full():
                    self.queue_step.append(j)
                else:
                    lost_count += 1
        return self.result, lost_count
