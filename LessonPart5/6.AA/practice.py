import sys

sys.stdin = open("input.txt", "rt")


def DFS(x):
    if x == m:
        print(res)
    else:
        for i in range(1, n + 1):
            res[x] = i
            DFS(x + 1)


n, m = map(int, input().split())
res = [0] * m
DFS(0)
