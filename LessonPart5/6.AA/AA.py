import sys

sys.stdin = open("input.txt", "rt")


def DFS(v):
    global cnt
    if v == m:
        cnt += 1
        print(res)
    else:
        for i in range(1, n + 1):
            res[v] = i
            DFS(v + 1)


n, m = map(int, input().split())
res = [0] * m
cnt = 0
DFS(0)
print(cnt)
