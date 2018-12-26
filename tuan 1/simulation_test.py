from simulation import Simulation

sim = Simulation(5, 4, 7)
assert(hasattr(sim, "process_rate"))
assert(hasattr(sim, "min_req_rate"))
assert(hasattr(sim, "max_req_rate"))
assert(hasattr(sim, "run"))

lost_requests_rate = sim.run(100000)
print(lost_requests_rate)
assert(lost_requests_rate > 0.74)
assert(lost_requests_rate < 0.76)