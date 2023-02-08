# sumResult = []
# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             result.append(numbers[i])
#             result.append(numbers[j])
#             result.append(numbers[k])

#             sumResult.append(sum(result))
#             result = []


# sumResult.sort(reverse=True)
# print(sumResult)
# print(sumResult[K - 1])

import sys

sys.stdin = open("input.txt", "rt")


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


N, K = map(int, input().split())
numbers = list(map(int, input().split()))

result = combinations(numbers, 3)
result = list(map((lambda x: x[0] + x[1] + x[2]), result))
result = list(set(result)) # << 이거 한줄..추가하기 ;;;; 문제 잘 읽자...
result.sort(reverse=True)
print(result[K - 1])
