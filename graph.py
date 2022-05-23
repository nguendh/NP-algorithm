import matplotlib.pyplot as graph
from benchmark import brute_force_time
from benchmark import bellman_time
from benchmark import inc_time


size = [1000*(i + 1) for i in range(4)]
graph.plot(size, brute_force_time, label="Brute Force Solution")
graph.plot(size, bellman_time, label="Bellman Held Karp Solution")
graph.plot(size, inc_time, label="Inclusion Exclusion Solution")
graph.legend()
graph.show()
