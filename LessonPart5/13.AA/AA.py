import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    src, dest = map(int, input().split())
    graph[src][dest] = 1

stack = []
stack.append(1)
distance = [0] * (n + 1)
distance[1] = 1

while stack:
    print(stack)
    src = stack.pop()
    for dest, cost in enumerate(graph[src]):
        if distance[dest] == 0 and cost == 1:
            distance[dest] = distance[src] + 1
            stack.append(dest)

print(distance)
