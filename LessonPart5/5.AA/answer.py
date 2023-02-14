import sys

sys.stdin = open("input.txt", "rt")


def DFS(L, sum, tsum):
    global max
    if sum + (total - tsum) < max:
        return
    if sum > c:
        return
    if L == n:
        if sum > max:
            max = sum
    else:
        DFS(L + 1, sum + weights[L], tsum + weights[L])
        DFS(L + 1, sum, tsum + weights[L])


c, n = map(int, input().split())

weights = [0] * (n)
for i in range(n):
    weights[i] = int(input())

total = sum(weights)

max = -2147000000

DFS(0, 0, 0)
print(max)
