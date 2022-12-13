import csv

with open("datasets/HMCampusGraph.csv", "r") as f:
    graph = csv.reader(f)
    next(graph)
    g = list(graph)


first = "Olshan"
final = "B02L"

bfs_visited = []
bfs_adjacent = []
bfs_backpath = {}
bfs_route = []

def bfs(visited, first, final):
    start = ""
    end = ""
    for i in range(len(g)):
        if g[i][1] == first:
            start = g[i][0]
        if g[i][1] == final:
            end = g[i][0]
    visited.append(start)
    #print("visited" , visited)
    bfs_adjacent.append(start)
   #print("adj", adjacent)
    bfs_backpath[start] = start
    #print("backpath", backpath)
    while bfs_adjacent:
        m = bfs_adjacent.pop(0)
        #print(m)
        for neighbour in g[int(m)][2].split(","):
            if neighbour not in visited:
                bfs_backpath[neighbour] = m
                if neighbour == end:
                    #print("found!")
                    bfs_route.append(g[int(neighbour)][1])
                    #print(neighbour)
                    
                    while bfs_backpath[neighbour] != neighbour:
                     
                        bfs_route.append(g[int(bfs_backpath[neighbour])][1])
                        neighbour = bfs_backpath[neighbour]

                
                visited.append(neighbour)
                bfs_adjacent.append(neighbour)
    bfs_route.reverse()
    return bfs_route

print(bfs(bfs_visited, first, final))

dfs_visited = []
dfs_backpath = {}
dfs_route = []

def dfs(visited, first, final, parent = 0):
    start_index = ""
    end_index = ""
    if len(visited) == 0:    
        for i in range(len(g)):
            if g[i][1] == first:
                start_index = g[i][0]
                parent =  g[i][0]
                #print("start",start_index)
            if g[i][1] == final:
                end_index = g[i][0]
                #print("end",end_index)
    else:
        start_index = first
        end_index = final
    if start_index not in visited:
        dfs_backpath[start_index] = parent
        #backpath[]
        if start_index == end_index:
            #print("found it!")
            #print(backpath)
            dfs_route.append(g[int(start_index)][1])
            while dfs_backpath[start_index] != start_index:
                     
                        dfs_route.append(g[int(dfs_backpath[start_index])][1])
                        start_index = dfs_backpath[start_index]
            dfs_route.reverse()
            if dfs_route.count != 0:
                #print("hi")
                print(dfs_route)
               # return dfs_route
            else:
                return None

        #print("str" ,start_index)
        visited.append(start_index)
        for neighbour in g[int(start_index)][2].split(","):
            dfs(visited, neighbour, end_index, start_index)
#print(g)

dfs(dfs_visited, first, final)