import csv

with open("datasets/HMCampusGraph.csv", "r") as f:
    graph = csv.reader(f)
    next(graph)
    g = list(graph)


visited = []
adjacent = []
backpath = {}
route = []

def bfs(graph, visited, first, final):
    start = ""
    end = ""
    for i in range(len(g)):
        if g[i][1] == first:
            start = g[i][0]
        if g[i][1] == final:
            end = g[i][0]
    visited.append(start)
    #print("visited" , visited)
    adjacent.append(start)
   #print("adj", adjacent)
    backpath[start] = start
    #print("backpath", backpath)
    while adjacent:
        m = adjacent.pop(0)
        #print(m)
        for neighbour in g[int(m)][2].split(","):
            if neighbour not in visited:
                backpath[neighbour] = m
                if neighbour == end:
                    #print("found!")
                    route.append(g[int(neighbour)][1])
                    #print(neighbour)
                    
                    while backpath[neighbour] != neighbour:
                     
                        route.append(g[int(backpath[neighbour])][1])
                        neighbour = backpath[neighbour]

                
                visited.append(neighbour)
                adjacent.append(neighbour)
    route.reverse()
    return route

first = "Olshan"
final = "B02L"
print(bfs(graph, visited, first, final))
    
#print(g)
