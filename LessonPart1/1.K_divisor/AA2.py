import sys

# sys.stdin = open("input.txt", "rt", encoding="utf-8")

N, K = map(int, input().split())
result = []


def solution(n, k):
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    if k > len(result):
        return -1

    return result[k - 1]


print(solution(N, K))
