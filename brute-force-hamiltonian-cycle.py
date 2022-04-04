import itertools

###Brute-Force Search Algorithm

###Basic Algorithm

### c ← first(P)
### while c ≠ Λ do
###     if valid(P,c) then
###         output(P, c)
###     c ← next(P, c)
### end while

### In order candidate for P after the current one c.

### valid (P, c): check whether candidate c is a solution for P.

### output (P, c): use the solution c of P as appropriate to the application.

### The next procedure must also tell when there are no more candidates for the instance P, after the current one c. 
### A convenient way to do that is to return a "null candidate", some conventional data value Λ that is distinct 
### from any real candidate. Likewise the first procedure should return Λ if there are no candidates at all for the instance P.

###The brute-force method is then expressed by the algorithm

### So in this problem P is all possible combinations of nodes and the validation is if the all consecutive nodes 
### also the first and the last nodes has connection(edge).

class Graph:
    def __init__(self,node_number):
        self.matrix = [[0 for j in range(node_number)] for i in range(node_number)]
        self.node_number = node_number
    def set_matrix(self,matrix):
        self.matrix = matrix
    def get_matrix(self):
        return self.matrix

class Brute_Force_Solution:
    def __init__(self,print_inf,graph):
        if print_inf:
            print("In computer science, brute-force search is a problem-solving technique")
            print("and algorithmic paradigm that consists of systematically enumerating")
            print("all possible candidates for the solution and checking whether each candidate satisfies the problem's statement.")
        self.graph = graph
    def find_hamilton_cycle(self):
        possible_node_combination = list(itertools.permutations(range(self.graph.node_number)))
        matrix = self.graph
        hamilton_cycle = True
        for i in possible_node_combination:
            for j in range(1,len(i)+1):
                if self.graph.matrix[i[j-1]][i[j%len(i)]] != 0:
                    hamilton_cycle = True 
                else:
                    hamilton_cycle = False
                    break
            if hamilton_cycle == True:
                break
        print(hamilton_cycle)

### Lets try with an example to check solution

a = Graph(6)
a.set_matrix([[0, 6, 0, 0, 0, 0], [0, 0, 6, 0, 0, 0], [0, 0, 0, 6, 0, 0], [0, 0, 0, 0, 6, 0], [0, 0, 0, 0, 0, 6], [6, 0, 0, 0, 0, 0]])
c = Brute_Force_Solution(False,a)
c.find_hamilton_cycle()