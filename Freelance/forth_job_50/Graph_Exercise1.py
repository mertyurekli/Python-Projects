from collections import defaultdict
import sys
N = int(input("Enter N (max node index): "))
q = int(input("Enter edge count: "))
print("Enter edges and weights in syntax \"edge1 edge2 weight\" where (edge1--weight-->edge2)")
edges = []
graph = defaultdict(list)
primGraph = [[0 for column in range(N)]
                      for row in range(N)]
for i in range(q):
    edge = input().split()
    a = int(edge[0])
    b = int(edge[1])
    w = int(edge[2])
    edges.append([a, b])
    graph[a].append(b)
    primGraph[a][b] = w
    primGraph[b][a] = w
cycles = []
# print(*primGraph, sep="\n")

def main():
    global edges
    global cycles
    global N
    global primGraph
    for edge in edges:
        for node in edge:
            findNewCycles([node])
    print("\n\nCYCLES\n----------------")
    print(len(cycles))
    for cy in cycles:
        path = [str(node) for node in list(reversed(cy))]
        s = ",".join(path)
        print(s)
    print("\n\nDFS\n----------------")
    for node in range(N):
        dfs(set(), graph, node)
        print()
    print("\n\nPRIM'S Algorithm\n----------------")
    primMST(N, primGraph)

def findNewCycles(path):
    start_node = path[0]
    next_node= None
    sub = []

    #visit each edge and each node of each edge
    for edge in edges:
        if edge[0] == start_node:
            next_node = edge[1]
            if not visitedf(next_node, path):
                # neighbor node not on path yet
                sub = [next_node]
                sub.extend(path)
                # explore extended path
                findNewCycles(sub)
            elif len(path) > 2  and next_node == path[-1]:
                # cycle found
                p = rotate_to_smallest(path)
                inv = invert(p)
                if isNew(p) and isNew(inv):
                    cycles.append(p)


def invert(path):
    return rotate_to_smallest(path[::-1])

#  rotate cycle path such that it begins with the smallest node
def rotate_to_smallest(path):
    n = path.index(min(path))
    return path[n:]+path[:n]

def isNew(path):
    return not path in cycles

def visitedf(node, path):
    return node in path

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" -> ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# A utility function to print the constructed MST stored in parent[]
def printMST(parent):
    print("Edge \tWeight")
    for i in range(1, N):
        print(parent[i], "-", i, "\t", primGraph[i][parent[i]])

# A utility function to find the vertex with
# minimum distance value, from the set of vertices
# not yet included in shortest path tree
def minKey(key, mstSet):

    # Initialize min value
    min = sys.maxsize

    for v in range(N):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v

    return min_index

# Function to construct and print MST for a graph
# represented using adjacency matrix representation
def primMST(N, primGraph):

    # Key values used to pick minimum weight edge in cut
    key = [sys.maxsize] * N
    parent = [None] * N  # Array to store constructed MST
    # Make key 0 so that this vertex is picked as first vertex
    key[0] = 0
    mstSet = [False] * N

    parent[0] = -1  # First node is always the root of

    for cout in range(N):

        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = minKey(key, mstSet)

        # Put the minimum distance vertex in
        # the shortest path tree
        mstSet[u] = True
        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shortest path tree
        for v in range(N):

            # graph[u][v] is non zero only for adjacent vertices of m
            # mstSet[v] is false for vertices not yet included in MST
            # Update the key only if graph[u][v] is smaller than key[v]
            if (primGraph[u][v] > 0 and mstSet[v] == False and key[v] > primGraph[u][v]):
                key[v] = primGraph[u][v]
                parent[v] = u

    printMST(parent)


main()

"""

10
15
1 2 5
1 8 10
1 6 6
2 3 4
2 6 1
5 0 11
5 7 3
5 3 1
6 7 2
6 5 7
7 1 9
8 5 5
8 0 4
9 5 2
4 9 1

"""
