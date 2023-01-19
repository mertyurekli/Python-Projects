##############  FUNCTIONS  #################
def cycle_finder(path):
    global cycles
    svertex = path[0]
    nvertex= None
    sub = []

    for edge in edges:
        if edge[0] == svertex:
            nvertex = edge[1]
            if not (nvertex in path):                # neighbor vertex not on path yet
                sub = [nvertex]
                sub.extend(path)
                cycle_finder(sub)                   # explore extended path
            elif len(path) > 2  and nvertex == path[-1]:                # cycle found
                p = rotate(path)
                inv = rotate(path[::-1])
                if (not p in cycles) and (not inv in cycles):
                    cycles.append(p)


def rotate(path):
    n = path.index(min(path))
    return path[n:]+path[:n]


def dfs(visited, graph, vertex):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbour in graph[vertex]:
            dfs(visited, graph, neighbour)


def printMST(parent):
    for i in range(1, N):
        print(parent[i], "-", i, "  :", primGraph[i][parent[i]])


def minKey(key, mstSet):
    min = 999999999     # Initialize min value

    for v in range(N):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v

    return min_index


def primMST(N, primGraph):
    key = [9999999] * N     # Key values used to pick minimum weight edge in cut
    parent = [None] * N  # Array to store constructed MST
    key[0] = 0      # Make key 0 so that this vertex is picked as first vertex
    mstSet = [False] * N
    parent[0] = -1  # First vertex is always the root of

    for cout in range(N):
        u = minKey(key, mstSet)
        mstSet[u] = True
        for v in range(N):
            if (primGraph[u][v] > 0 and mstSet[v] == False and key[v] > primGraph[u][v]):
                key[v] = primGraph[u][v]
                parent[v] = u

    printMST(parent)

####################################################################


##############  VARIABLES  #################
N = 10
edges = [[1, 2], [1, 8], [1, 6], [2, 3], [2, 6], [4, 2], [5, 0], [5, 7], [5, 3], [6, 7], [6, 5], [7, 1], [8, 5], [8, 0], [9, 5]]
graph = {
            0: [],
            1: [2, 8, 6], 
            2: [3, 6], 
            3: [],
            4: [2], 
            5: [0, 7, 3], 
            6: [7, 5], 
            7: [1], 
            8: [5, 0], 
            9: [5]
        }
primGraph = [
            [0, 0, 0, 0, 0, 10, 0, 0, 15, 0],
            [0, 0, 1, 0, 0, 0, 2, 3, 13, 0],
            [0, 1, 0, 5, 6, 0, 4, 0, 0, 0],
            [0, 0, 5, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
            [10, 0, 0, 8, 0, 0, 7, 12, 14, 9],
            [0, 2, 4, 0, 0, 7, 0, 11, 0, 0],
            [0, 3, 0, 0, 0, 12, 11, 0, 0, 0],
            [15, 13, 0, 0, 0, 14, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 9, 0, 0, 0, 0]
        ]

####################################################################
cycles = []

for edge in edges:
    for vertex in edge:
        cycle_finder([vertex])
print("Count of cycles : ", len(cycles))
print("Cycles :")
for cy in cycles:
    print(" - ".join([str(vertex) for vertex in cy]))

print("*******************************")
for vertex in range(N):
    dfs(set(), graph, vertex)
    print()
print("*******************************")
primMST(N, primGraph)
