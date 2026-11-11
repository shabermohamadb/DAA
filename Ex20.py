# Build a Max Heap
import heapq

a = list(map(int, input("Enter elements: ").split()))
heap = [-x for x in a]
heapq.heapify(heap)

print("Max Heap:", [-x for x in heap])
