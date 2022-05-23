import itertools
import numpy as np
import time

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


class Graph:
    def __init__(self, node_number):
        self.matrix = [[0 for j in range(node_number)] for i in range(node_number)]
        self.node_number = node_number

    def set_matrix(self, matrix): self.matrix = matrix

    def get_matrix(self):
        return self.matrix


class BruteForceSolution:
    def __init__(self, graph):
        self.graph = graph

    def find_hamilton_cycle(self):
        possible_node_combination = list(itertools.permutations(range(self.graph.node_number)))
        matrix = self.graph
        hamilton_cycle = True
        for i in possible_node_combination:
            for j in range(1, len(i) + 1):
                if self.graph.matrix[i[j - 1]][i[j % len(i)]] != 0:
                    hamilton_cycle = True
                else:
                    hamilton_cycle = False
                    break
            if hamilton_cycle:
                break
        print(hamilton_cycle)


class BellmanHeldKarp:
    def __init__(self, graph):
        self.graph = graph

    def find_hamilton_cycle(self):
        path = [[0 for j in range(self.graph.node_number)] for i in range(pow(2, self.graph.node_number) + 1)]
        for i in range(0, self.graph.node_number - 1):
            path[(1 << i)][i] = (self.graph.matrix[0][i + 1] or self.graph.matrix[i + 1][0])
        for S in range(2, self.graph.node_number):
            for s in range(1, pow(2, self.graph.node_number - 1)):
                if count_set_bits(s) == S:
                    for i in range(0, self.graph.node_number - 1):
                        if (s >> i) & 1:
                            for j in range(0, self.graph.node_number - 1):
                                if ((s >> j) & 1) and (i != j):
                                    path[s][i] |= (path[(1 << i) ^ s][j] and (
                                            self.graph.matrix[j + 1][i + 1] or self.graph.matrix[i + 1][j + 1]))
        result = False
        for i in range(1, self.graph.node_number - 1):
            result |= (path[pow(2, self.graph.node_number - 1) - 1][i - 1] and (
                    self.graph.matrix[i][0] or self.graph.matrix[0][i]))
        print(bool(result))


class InclExcl:
    def __init__(self, graph):
        self.graph = graph

    def calculate(self, matrix, vector):
        if len(vector) == 1:
            return np.multiply(matrix, matrix[vector[0]])
        else:
            a = vector[1:]
            return self.calculate(matrix, np.array([vector[0]])) + self.calculate(matrix, a)

    def find_hamilton_cycle(self):
        matrix = self.graph
        hamilton_cycle = True
        labels = np.random.choice(range(0, matrix.node_number), int(matrix.node_number / 2), replace=False)
        matrix_old = matrix.get_matrix() + self.calculate(matrix.get_matrix(), labels)
        matrix_new = np.ones((int(matrix.node_number / 2), int(matrix.node_number / 2)))
        iter = int(matrix.node_number / 2) - 1
        for i in range(0, int(matrix.node_number / 2)):
            for j in range(0, int(matrix.node_number / 2)):
                matrix_new[i][j] = np.linalg.det(matrix_old[iter * i:iter * i + 2, iter * j:iter * j + 2])
        if np.linalg.det(matrix_new) == 0:
            hamilton_cycle = False
        print(hamilton_cycle)


class TimeCalculating:
    def __init__(self, graph):
        self.graph = graph

    def time_calculating(self):
        first_time = 0
        start = time.time()
        brute_force = BruteForceSolution(self.graph)
        brute_force.find_hamilton_cycle()
        end = time.time()
        first_time += (end - start)
        print("Time for brute force solution:", first_time)

        second_time = 0
        start = time.time()
        bellman = BellmanHeldKarp(self.graph)
        bellman.find_hamilton_cycle()
        end = time.time()
        second_time += (end - start)
        print("Time for Bellman Held Karp:", second_time)

        third_time = 0
        start = time.time()
        inclexcl = InclExcl(self.graph)
        inclexcl.find_hamilton_cycle()
        end = time.time()
        third_time += (end - start)
        print("Time for Inclusion Exclusion:", third_time)


### Lets try with an example to check solution

a = Graph(6)
a.set_matrix([[0, 1, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 0, 1, 0, 0],
              ])
e = TimeCalculating(a)
e.time_calculating()
