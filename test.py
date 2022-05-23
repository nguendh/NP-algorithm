import unittest
import random

from main import BruteForceSolution
from main import BellmanHeldKarp
from main import InclExcl
from main import Graph


class Test(unittest.TestCase):
    def test_case1(self):
        size = random.randint(1, 1000)
        random_list = [[random.randint(0, 1) for i in range(size)] for j in range(size)]
        graph = Graph(size)
        graph.set_matrix(random_list)
        brute_force = BruteForceSolution(graph)
        bellman = BellmanHeldKarp(graph)
        inc = InclExcl(graph)
        self.assertEqual(brute_force.find_hamilton_cycle(), bellman.find_hamilton_cycle(), inc.find_hamilton_cycle())

    def test_case2(self):
        random_list = [[1 for i in range(1000)] for j in range(1000)]
        graph = Graph(1000)
        graph.set_matrix(random_list)
        brute_force = BruteForceSolution(graph)
        bellman = BellmanHeldKarp(graph)
        inc = InclExcl(graph)
        self.assertEqual(brute_force.find_hamilton_cycle(), True)
        self.assertEqual(bellman.find_hamilton_cycle(), True)
        self.assertEqual(inc.find_hamilton_cycle(), True)

    def test_case3(self):
        random_list = [[0 for i in range(1000)] for j in range(1000)]
        graph = Graph(1000)
        graph.set_matrix(random_list)
        brute_force = BruteForceSolution(graph)
        bellman = BellmanHeldKarp(graph)
        inc = InclExcl(graph)
        self.assertEqual(brute_force.find_hamilton_cycle(), True)
        self.assertEqual(bellman.find_hamilton_cycle(), True)
        self.assertEqual(inc.find_hamilton_cycle(), True)

    def test_case4(self):
        random_list = [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0],
                       [0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 1],
                       [1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0],
                       ]
        size = len(random_list)
        graph = Graph(size)
        graph.set_matrix(random_list)
        brute_force = BruteForceSolution(graph)
        bellman = BellmanHeldKarp(graph)
        inc = InclExcl(graph)
        self.assertEqual(brute_force.find_hamilton_cycle(), True)
        self.assertEqual(bellman.find_hamilton_cycle(), True)
        self.assertEqual(inc.find_hamilton_cycle(), True)
