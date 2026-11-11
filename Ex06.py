# Dijkstra's Algorithm - Shortest Path Between Two Vertices
n = int(input("Vertices: "))
a = [list(map(int, input().split())) for _ in range(n)]
source = int(input("Source: "))
target = int(input("Destination: "))

dist = [float("inf")] * n
parent = [-1] * n
visited = [False] * n
dist[source] = 0

for _ in range(n):
    u = -1
    for i in range(n):
        if not visited[i] and (u == -1 or dist[i] < dist[u]):
            u = i
    if u == -1 or dist[u] == float("inf"):
        break
    visited[u] = True

    for v in range(n):
        if a[u][v] > 0 and dist[v] > dist[u] + a[u][v]:
            dist[v] = dist[u] + a[u][v]
            parent[v] = u

if dist[target] == float("inf"):
    print("No path")
else:
    path = []
    v = target
    while v != -1:
        path.append(v)
        v = parent[v]
    print("Shortest Path:", path[::-1])
    print("Cost:", dist[target])
