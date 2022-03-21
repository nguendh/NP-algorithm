# The proof why is the Hamiltonian cycle is in NP class

If any problem is in NP, then this problem must have a solution that can be checked in polynomial time.

We can check the solution by checking whether all the vertices belong to the graph and each pair of vertices belonging to the solution are adjacent. 

This can be done in polynomial time.

# Description

A Hamiltonian cycle is a closed loop on a graph where every node (vertex) is visited exactly once.

A loop is just an edge that joins a node to itself; so a Hamiltonian cycle is a path traveling from a point back to itself, visiting every node en route.

The Hamiltonian cycle problem is the problem of determining whether a Hamiltonian cycle exists in a given graph (whether directed or undirected).


# Ways to solve it

## The three ways are listed here to solve this problem:

### 1.There is a way to solve the Hamiltonian cycle problem via a brute force search algorithm that tests all possible sequence.

The algorithms is shown:

Begin
   if all nodes are included, then
      if there is an edge between nodes k and 0, then
         return true
      else
         return false;

   for all vertex v except starting point, do
      if isValid(v, k), then //when v is a valid edge
         add v into the path
         if cycleFound(k+1) is true, then
            return true
         otherwise remove v from the path
   done
   return false
End

### 2.Also, there is a way to solve via a dynamic programming algorithm that the algorithm is called Bellman–Held–Karp algorithm.

The algorithm is shown:

function algorithm TSP (G, n) is
    for k := 2 to n do
        g({k}, k) := d(1, k)
    end for

    for s := 2 to n−1 do
        for all S ⊆ {2, ..., n}, |S| = s do
            for all k ∈ S do
                g(S, k) := minm≠k,m∈S [g(S\{k}, m) + d(m, k)]
            end for
        end for
    end for

    opt := mink≠1 [g({2, 3, ..., n}, k) + d(k, 1)]
    return (opt)
end function 

### 3.Andreas Björklund provided an alternative approach using the inclusion–exclusion principle to reduce the problem of counting the number of Hamiltonian cycles to a simpler counting problem, of counting cycle covers, which can be solved by computing certain matrix determinants.

# Complexities

The complexity of solving via a brute force search algorithm is n!, Bellman–Held–Karp algorithm's complexity is O(n2 2n), and the complexity of solving via using the inclusion–exclusion principle is O(1.657n).
