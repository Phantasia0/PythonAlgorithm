import sys

sys.stdin = open("input.txt", "rt")


def DFS(L, sums, t):
    global res
    if L == n + 1:
        if sums > res:
            res = sums
    else:
        DFS(L + 1, sums + pv[L], t + pt[L])
        DFS(L + 1, sums, t)


n = int(input())

pv = list()
pt = list()

for i in range(n):
    a, b = map(int, input().split())
    pt.append(a)
    pv.append(b)

check = [0] * n
res = -2222222222
DFS(0, 0, 0)
print(res)
