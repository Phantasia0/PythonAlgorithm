import sys

sys.stdin = open("input.txt", "rt")


def permutations(arr, n):
    if n == 1:
        return list(map(lambda v: [v], arr))

    result = []

    for idx, fixed in enumerate(arr):
        rest = list(filter((lambda v: arr.index(v) != idx), arr))

        perms = permutations(rest, n - 1)
        combine = list(map((lambda x: [fixed, *x]), perms))
        result.extend(combine)

    return result


n, m = map(int, input().split())

nums = [i for i in range(1, n + 1)]
res = permutations(nums, m)
for i in res:
    for j in range(m):
        print(i[j], end=" ")
    print()
print(len(res))
