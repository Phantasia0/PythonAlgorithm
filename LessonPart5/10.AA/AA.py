import sys

sys.stdin = open("input.txt", "rt")


def combinations(arr, n):
    if n == 1:
        return list([v] for v in arr)

    result = []

    for idx, fixed in enumerate(arr):
        rest = arr[idx + 1 :]

        combins = combinations(rest, n - 1)
        combine = list(map((lambda v: [fixed, *v]), combins))
        result.extend(combine)
    return result


N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]

res = combinations(nums, M)

for i in res:
    for j in range(len(i)):
        print(i[j], end=" ")
    print()

print(len(res))
