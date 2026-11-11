# Heap Sort - Ascending Order
import heapq

a = list(map(int, input("Enter elements: ").split()))
heapq.heapify(a)

print("Ascending:", end=" ")
while a:
    print(heapq.heappop(a), end=" ")
print()
