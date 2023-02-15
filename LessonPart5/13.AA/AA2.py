import sys

# sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())


def DFS(L):
    global cnt
    if L == n:
        # for x in res:
        #     print(x, end=" ")
        # print()
        cnt += 1
    else:
        for dest, cost in enumerate(graph[L]):
            if cost == 1:
                if check[dest] == 0:
                    check[dest] = 1
                    res.append(dest)
                    DFS(dest)
                    check[dest] = 0
                    res.pop()


graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    src, dest = map(int, input().split())
    graph[src][dest] = 1

check = [0] * (n + 1)
check[1] = 1
res = [1]
cnt = 0

DFS(1)
print(cnt)
