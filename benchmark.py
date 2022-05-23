from timeit import default_timer as time
import random
import sys
import threading
from main import BruteForceSolution
from main import BellmanHeldKarp
from main import InclExcl
from main import Graph

number_of_test = 7
brute_force_time = list()
bellman_time = list()
inc_time = list()


class TimeCalculating:
    @staticmethod
    def time_calculating():
        given_list = [[[random.randint(0, 1) for i in range(2 + k)] for j in range(2 + k)]
                      for k in range(number_of_test)]
        for k in range(number_of_test):
            first_average_time = 0
            graph = Graph(len(given_list[k]))
            graph.set_matrix(given_list[k])
            start = time()
            brute_force = BruteForceSolution(graph)
            brute_force.find_hamilton_cycle()
            interval = time() - start
            first_average_time += interval

            print(f"Time for brute force solution for {len(given_list[k])} numbers",
                  first_average_time / len(given_list[k]))

            brute_force_time.append(first_average_time / len(given_list[k]))

        for k in range(number_of_test):
            second_average_time = 0
            graph = Graph(len(given_list[k]))
            graph.set_matrix(given_list[k])
            start = time()
            bellman = BellmanHeldKarp(graph)
            bellman.find_hamilton_cycle()
            interval = time() - start
            second_average_time += interval

            print(f"Time for Bellman Held Karp solution for {len(given_list[k])} numbers",
                  second_average_time / len(given_list[k]))

            bellman_time.append(second_average_time / len(given_list[k]))

        for k in range(number_of_test):
            third_average_time = 0
            graph = Graph(len(given_list[k]))
            graph.set_matrix(given_list[k])
            start = time()
            inc = InclExcl(graph)
            inc.find_hamilton_cycle()
            interval = time() - start
            third_average_time += interval

            print(f"Time for Inclusion Exclusion solution for {len(given_list[k])} numbers",
                  third_average_time / len(given_list[k]))

            inc_time.append(third_average_time / len(given_list[k]))


sys.setrecursionlimit(10 ** 8)
threading.stack_size(2 ** 26)
threading.Thread(target=TimeCalculating.time_calculating()).start()
