import sys

sys.stdin = open("input.txt", "rt")


def permutations(arr, n):
    if n == 1:
        return [[v] for v in arr]

    result = []

    for idx, fixed in enumerate(arr):
        rest = list(filter(lambda x: arr.index(x) != idx, arr))

        perms = permutations(rest, n - 1)
        combine = list(map(lambda v: [fixed, *v], perms))
        result.extend(combine)

    return result


def DFS(L, arr):
    global fsum
    result = []
    if L == n:
        fsum = arr[0]
    else:
        for i in range(n - L):
            if arr[i] + arr[i + 1] > f:
                return
            result.append(arr[i] + arr[i + 1])
        DFS(L + 1, result)
        return


n, f = map(int, input().split())
fsum = 0

res = [i for i in range(1, n + 1)]
lists = permutations(res, n)
for li in lists:
    DFS(1, li)
    if fsum == f:
        for i in range(n):
            print(li[i], end=" ")
        break
