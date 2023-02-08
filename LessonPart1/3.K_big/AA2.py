arr = [1, 2, 3, 4]


def combinations(arr, n):
    if n == 1:
        return list(map((lambda v: [v]), arr))
    result = []

    for idx, fixed in enumerate(arr):
        rest = arr[idx + 1 :]

        combins = combinations(rest, n - 1)
        combine = list(map((lambda v: [fixed, *v]), combins))
        result.extend(combine)

    return result


def permutations(arr, n):
    if n == 1:
        return list(map((lambda v: [v]), arr))
    result = []

    for idx, fixed in enumerate(arr):
        rest = list(filter((lambda v: arr.index(v) != idx), arr))

        perms = permutations(rest, n - 1)
        combine = list(map((lambda v: [fixed, *v]), perms))
        result.extend(combine)

    return result


print(permutations(arr, 2))
