import csv

# Stores adjacency list as a list of lists. Index of vertex corresponds with its location in the list
with open("datasets/HMCampusGraph.csv", "r") as f:
    graph = csv.reader(f)
    next(graph)
    g = list(graph)


# Set starting and ending vertexes. These can be changed.
first = "Olshan"
final = "B02L"


# Initialize bfs variables

# The visited vertexes
bfs_visited = []

# The unexplored neighbours of the visited vertexes: vertexes who have neighbours that haven't been visited
bfs_adjacent = []

# Dictionary that stores the vertex used to access another vertex. Child : Parent
bfs_backpath = {}

# Final route
bfs_route = []

# BFS is implemented iteratively. 
# The starting vertex is added to the visited & adjacent lists, 
# then all of its neighbours are added to the visited & adjacent lists,
# then the same for the neighbours of the vertexes on the adjacent list,
# and so on until the final vertex is found
def bfs(visited, first, final):
    # Find the indexes of the first & final vertexes.
    start = ""
    end = ""
    for i in range(len(g)):
        if g[i][1] == first:
            start = g[i][0]
        if g[i][1] == final:
            end = g[i][0]
    visited.append(start)
    bfs_adjacent.append(start)
    # Starting vertex links back to itself. This is used to determine the starting vertex later.
    bfs_backpath[start] = start
    # For all vertexes in the adjacent list, remove it, find its neighbours, and add them to the visited and adjacent list.
    while bfs_adjacent:
        m = bfs_adjacent.pop(0)
        for neighbour in g[int(m)][2].split(","):
            if neighbour not in visited:
                # Set parent in backpath
                bfs_backpath[neighbour] = m
                if neighbour == end:
                    bfs_route.append(g[int(neighbour)][1])
                    # This while loop backtracks through the backpath dictionary, starting with the final vertex
                    # until the first vertex is reached
                    while bfs_backpath[neighbour] != neighbour:
                        bfs_route.append(g[int(bfs_backpath[neighbour])][1])
                        neighbour = bfs_backpath[neighbour]
                visited.append(neighbour)
                bfs_adjacent.append(neighbour)
    # The resulting route goes from the final -> first, so flip it
    bfs_route.reverse()
    print(bfs_route) 

bfs(bfs_visited, first, final)


# Initialize dfs variables

# The visited vertexes
dfs_visited = []

# Dictionary that stores the vertex used to access another vertex. Child : Parent
dfs_backpath = {}

# Final route
dfs_route = []

# DFS is implemented recursively. 
# It calls itself on the neighbours of the starting vertex, and then on their neighbours,
# and so on until it finds the final vertex.
def dfs(visited, first, final, parent = -1):
    # Find the start and end indexes. On the first call, it finds the indexes for the names
    # of the first and final indexes. On subsequent calls, it passes forward the current index
    # as the "first" index
    start_index = ""
    end_index = ""
    if len(visited) == 0:    
        for i in range(len(g)):
            if g[i][1] == first:
                start_index = g[i][0]
                # parent is used to keep track of the previous vertex
                parent =  g[i][0]
            if g[i][1] == final:
                end_index = g[i][0]
    else:
        start_index = first
        end_index = final
    if start_index not in visited:
        dfs_backpath[start_index] = parent
        if start_index == end_index:
            dfs_route.append(g[int(start_index)][1])
            # This while loop backtracks through the backpath dictionary, starting with the final vertex
            # until the first vertex is reached
            while dfs_backpath[start_index] != start_index:
                        dfs_route.append(g[int(dfs_backpath[start_index])][1])
                        start_index = dfs_backpath[start_index]
            # The resulting route goes from the final -> first, so flip it
            dfs_route.reverse()

            # Once we have an answer, print it
            if dfs_route.count != 0:
                print(dfs_route)
            else:
                return None
        visited.append(start_index)
        # for each neighbour, recursively call dfs. This allows the algorithm to follow a path until it hits a dead-end,
        # backtrack, and then keep going
        for neighbour in g[int(start_index)][2].split(","):
            # The neighbour takes the place of the "first" index, and the old first index becomes the parent
            dfs(visited, neighbour, end_index, start_index)

dfs(dfs_visited, first, final)


# Following code is modified BFS used to find eccentricity of the graph
ecc_visited = []

ecc_adjacent = []

ecc_backpath = {}


def eccentricity(visited, start):
    length = 1
    visited.append(start)
    ecc_adjacent.append(start)
    while ecc_adjacent:
        m = ecc_adjacent.pop(0)
        for neighbour in g[int(m)][2].split(","):
            if neighbour not in visited:
                ecc_backpath[neighbour] = m
               # print(neighbour)
                visited.append(neighbour)
                ecc_adjacent.append(neighbour)

    last_neighbour = visited[-1]
    print("furthest away: " + last_neighbour)
    while ecc_backpath[last_neighbour] != start:
            length += 1
            last_neighbour = ecc_backpath[last_neighbour]
        
    print("length =", length)

#eccentricity(ecc_visited, 147)
