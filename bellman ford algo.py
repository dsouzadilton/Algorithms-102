V, src = 5,0

graph = []
dist = []

graph.append([0, 1, -1])
graph.append([0, 2, 4])
graph.append([1, 2, 3])
graph.append([1, 3, 2])
graph.append([1, 4, 2])
graph.append([3, 2, 5])
graph.append([3, 1, 1])
graph.append([4, 3, -3])

dist = [float("Inf")] * V
dist[src] = 0

for _ in range(V - 1): 
    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

for u, v, w in graph:
    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
        print("Graph contains negative weight cycle")
        exit(0)     

print("Vertex | Distance from Source")
for i in range(V):
    print("{0:2}{1} | {2:2}".format(i," "*4, dist[i]))
