# Warshall's Algorithm - Transitive Closure
n = int(input("Vertices: "))
a = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            a[i][j] = int(bool(a[i][j] or (a[i][k] and a[k][j])))

print("Transitive Closure:")
for row in a:
    print(*row)
