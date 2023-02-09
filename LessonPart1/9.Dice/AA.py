import sys

# sys.stdin = open("input.txt", "r")

n = int(input())


def calc(arr):
    array = [0] * 7
    score = 0
    for num in arr:
        array[num] += 1

    maxCount = max(array)

    if maxCount == 1:
        maxNum = float("-inf")
        for num in arr:
            if num > maxNum:
                maxNum = num
        score = maxNum * 100
    elif maxCount == 2:
        for num in arr:
            if array[num] == 2:
                score = 1000 + num * 100
    else:
        for num in arr:
            if array[num] == 3:
                score = 10000 + num * 1000

    return score


res = []
for i in range(n):
    numbers = list(map(int, input().split()))
    score = calc(numbers)
    res.append(score)

print(max(res))
