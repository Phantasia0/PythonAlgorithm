import sys

# sys.stdin = open("input.txt", "rt")


def DFS(L, sum):
    global max
    if sum > c:
        return

    if L == n:
        if max < sum <= c:
            max = sum
    else:
        DFS(L + 1, sum + weights[L])
        DFS(L + 1, sum)


c, n = map(int, input().split())

weights = [0] * (n)
for i in range(n):
    weights[i] = int(input())

max = 0

DFS(0, 0)
print(max)
