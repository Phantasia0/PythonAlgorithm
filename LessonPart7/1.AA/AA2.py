import sys


def DFS(L):
    if dy[L] > 0:
        return dy[L]
    if L == 1 or L == 2:
        return L
    else:
        dy[L] = DFS(L - 1) + DFS(L - 2)
        return dy[L]


sys.stdin = open("input.txt", "rt")
n = int(input())
dy = [0] * (n + 1)
print(DFS(n))
