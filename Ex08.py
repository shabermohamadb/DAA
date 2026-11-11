# Travelling Salesman Problem - Branch and Bound
n = int(input("Cities: "))
a = [list(map(int, input().split())) for _ in range(n)]
best = float("inf")
best_path = []

def tsp(city, path, cost):
    global best, best_path

    if cost >= best:
        return
    if len(path) == n:
        if a[city][0] > 0 and cost + a[city][0] < best:
            best = cost + a[city][0]
            best_path = path + [0]
        return

    for nxt in range(1, n):
        if nxt not in path and a[city][nxt] > 0:
            tsp(nxt, path + [nxt], cost + a[city][nxt])

tsp(0, [0], 0)
if best_path:
    print("Minimum Cost:", best)
    print("Optimal Route:", best_path)
else:
    print("No possible route")
