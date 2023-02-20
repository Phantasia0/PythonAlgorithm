import sys

sys.stdin = open("input.txt", "rt")


def DFS(L):
    if dy[L] > 0:
        return dy[L]

    if L == 1 or 2:
        return L
    else:
        dy[L] = DFS(L - 2) + DFS(L - 1)
        return dy[L]


n = int(input())
dy = [0] * (n + 1)
