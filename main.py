import itertools
import tkinter

import numpy as np
import time

from tkinter import Tk, Label, StringVar, Button, Entry, BOTTOM, RIGHT


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
        return hamilton_cycle


class BellmanHeldKarp:
    def __init__(self, graph):
        self.graph = graph

    def find_hamilton_cycle(self):
        matrix = self.graph
        path = [[0 for j in range(int(matrix.node_number))] for i in range(pow(2, int(matrix.node_number)) + 1)]
        for i in range(0, int(matrix.node_number - 1)):
            path[(1 << i)][i] = (matrix.matrix[0][i + 1] or matrix.matrix[i + 1][0])
        for S in range(2, int(matrix.node_number)):
            for s in range(1, pow(2, int(matrix.node_number - 1))):
                if count_set_bits(s) == S:
                    for i in range(0, int(matrix.node_number - 1)):
                        if (s >> i) & 1:
                            for j in range(0, int(matrix.node_number - 1)):
                                if ((s >> j) & 1) and (i != j):
                                    path[s][i] |= (path[(1 << i) ^ s][j] and (
                                            matrix.matrix[j + 1][i + 1] or matrix.matrix[i + 1][j + 1]))
        result = False
        for i in range(1, matrix.node_number - 1):
            result |= (path[pow(2, int(matrix.node_number - 1)) - 1][i - 1] and (
                    matrix.matrix[i][0] or matrix.matrix[0][i]))
        return bool(result)


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
                if i == j:
                    matrix_new[i][j] = np.linalg.det(matrix_old[iter * i:iter * i + 2, iter * j:iter * j + 2])
        if np.linalg.det(matrix_new) == 0:
            hamilton_cycle = False
        print(hamilton_cycle)


class Dirac:
    def __init__(self, graph):
        self.graph = graph

    def findDegree(self, ver):
        degree = 0
        for i in range(self.graph.node_number):
            if (self.graph.matrix[ver][i] == 1 or self.graph.matrix[ver][i] == 1):
                degree += 1
        return degree

    def find_hamilton_cycle(self):
        matrix = self.graph
        hamilton_cycle = True
        for i in range(matrix.node_number):
            if self.findDegree(i) <= (matrix.node_number / 2):
                hamilton_cycle = False
                break
        print(hamilton_cycle)
        if (hamilton_cycle == False):
            return BellmanHeldKarp(self.graph).find_hamilton_cycle()


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


window = Tk()
window.title("Hamilton")
window.geometry("650x500+120+120")
window.configure(bg='bisque2')
window.resizable(False, False)
NumberOfNode = Label(window, text="Enter number of nodes: ", font=('arial', 10, 'bold'), bg="bisque2")
NumberOfNode.pack()
T = tkinter.Text(window, height=1, width=5)
T.pack()
b1 = Button(window, text="Submit", command=lambda: mtx(int(T.get("1.0", "end-1c"))))
b1.pack()

text_var = []
entries = []
matrix = []


def get_mat():
    for i in range(int(T.get("1.0", "end-1c"))):
        matrix.append([])
        for j in range(int(T.get("1.0", "end-1c"))):
            matrix[i].append(int(text_var[i][j].get()))
    a = Graph(int(T.get("1.0", "end-1c")))
    a.set_matrix(matrix)
    b = BellmanHeldKarp(a)
    b.find_hamilton_cycle()
    c = BruteForceSolution(a)
    c.find_hamilton_cycle()
    d = Dirac(a)
    d.find_hamilton_cycle()
    Label(window, text="Brute Force Solution: " + str(c.find_hamilton_cycle()), font=('arial', 10, 'bold'),
          bg="bisque2").pack()
    Label(window, text="Bellman Held Karp Solution: " + str(b.find_hamilton_cycle()), font=('arial', 10, 'bold'),
          bg="bisque2").pack()
    Label(window, text="Dirac-Bellman Solution: " + str(d.find_hamilton_cycle()), font=('arial', 10, 'bold'),
          bg="bisque2").pack()


Label(window, text="Enter matrix: ", font=('arial', 10, 'bold'),
      bg="bisque2").place(x=20, y=20)


def mtx(number_of_node):
    x2 = 0
    y2 = 0
    rows, cols = (number_of_node, number_of_node)
    for i in range(rows):
        text_var.append([])
        entries.append([])
        for j in range(cols):
            text_var[i].append(StringVar())
            entries[i].append(Entry(window, textvariable=text_var[i][j], width=3))
            entries[i][j].place(x=60 + x2, y=80 + y2)
            x2 += 30
        y2 += 30
        x2 = 0
    button = Button(window, text="Submit", bg='bisque3', width=15, command=lambda: get_mat())
    button.pack(side=BOTTOM)


window.mainloop()


### Lets try with an example to check solution


# a.set_matrix([[0, 1, 0, 0, 1, 0],
#               [1, 0, 1, 0, 1, 0],
#               [0, 1, 0, 1, 0, 0],
#               [0, 0, 1, 0, 1, 1],
#               [1, 1, 0, 1, 0, 1],
#               [1, 0, 0, 0, 0, 0],
#               ])
# e = TimeCalculating(a)
# e.time_calculating()
# a.set_matrix(matrix)
# b = Dirac(a)
# b.find_hamilton_cycle()
# c = BruteForceSolution(a)
# c.find_hamilton_cycle()
