# Dijkstra's Algorithm - Shortest Paths from Source
n = int(input("Vertices: "))
a = [list(map(int, input().split())) for _ in range(n)]
source = int(input("Source: "))

dist = [float("inf")] * n
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

for i in range(n):
    print(i, "=", "INF" if dist[i] == float("inf") else dist[i])
