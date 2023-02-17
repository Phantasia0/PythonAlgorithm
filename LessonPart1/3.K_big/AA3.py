import sys

sys.stdin = open("input.txt", "rt")


def permutations(arr, n):
    if n == 1:
        return [[v] for v in arr]

    result = []

    for idx, fixed in enumerate(arr):
        rest = list(filter((lambda x: arr.index(x) != idx), arr))

        perms = permutations(rest, n - 1)
        combine = list(map((lambda v: [fixed, *v]), perms))
        result.extend(combine)

    return result


n, k = map(int, input().split())
cards = list(map(int, input().split()))
res = permutations(cards, 3)
sums = []

for i in res:
    sums.append(sum(i))

sumSet = set(sums)
sumSet = list(sumSet)

sumSet.sort(reverse=True)
print(sumSet[k - 1])
