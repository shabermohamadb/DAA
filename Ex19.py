# Topological Sort - User Input Vertices and Edges
n, e = map(int, input("Vertices Edges: ").split())
graph = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(e):
    u, v = map(int, input("Edge: ").split())
    graph[u].append(v)
    indegree[v] += 1

order = []
for _ in range(n):
    found = False
    for i in range(n):
        if indegree[i] == 0:
            order.append(i)
            indegree[i] = -1
            for j in graph[i]:
                indegree[j] -= 1
            found = True
            break
    if not found:
        break

if len(order) == n:
    print("Topological Order:", order)
else:
    print("Graph contains a cycle")
