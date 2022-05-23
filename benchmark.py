from timeit import default_timer as time
import random
import sys
import threading
from main import BruteForceSolution
from main import BellmanHeldKarp
from main import InclExcl
from main import Graph

number_of_test = 5
total_value = 5
brute_force_time = list()
bellman_time = list()
inc_time = list()


class TimeCalculating:
    @staticmethod
    def time_calculating():
        given_list = [[[random.randint(0, 1) for i in range(1000 * (k + 1))] for j in range(total_value)]
                      for k in range(number_of_test)]
        graph = Graph(total_value)
        for i in range(number_of_test):
            first_average_time = 0
            for j in range(total_value):
                graph.set_matrix(given_list[i])
                start = time()
                brute_force = BruteForceSolution(graph)
                brute_force.find_hamilton_cycle()
                interval = time() - start
                first_average_time += interval

            print(f"Time for brute force solution for {len(given_list)} numbers",
                  first_average_time / len(given_list[i]))

            brute_force_time.append(first_average_time / len(given_list[i]))

        for i in range(number_of_test):
            second_average_time = 0
            for j in range(total_value):
                graph.set_matrix(given_list[i])
                start = time()
                top_down = BellmanHeldKarp(given_list[i])
                top_down.find_hamilton_cycle()
                interval = time() - start
                second_average_time += interval

            print(f"Time for Bellman Held Karp solution for {len(given_list[i])} numbers",
                  second_average_time / len(given_list[i]))

            bellman_time.append(second_average_time / len(given_list[i]))

        for i in range(number_of_test):
            third_average_time = 0
            for j in range(total_value):
                graph.set_matrix(given_list[i])
                start = time()
                bottom_up = InclExcl(given_list[i])
                bottom_up.find_hamilton_cycle()
                interval = time() - start
                third_average_time += interval

            print(f"Time for Inclusion Exclusion solution for {len(given_list[i])} numbers",
                  third_average_time / len(given_list[i]))

            inc_time.append(third_average_time / len(given_list[i]))


sys.setrecursionlimit(10 ** 8)
threading.stack_size(2 ** 26)
threading.Thread(target=TimeCalculating.time_calculating()).start()
