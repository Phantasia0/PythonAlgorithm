import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
nums = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


result = []
for num in nums:
    result.append(digit_sum(num))

maxNum = max(result)

for num in nums:
    if maxNum == digit_sum(num):
        print(num)
        break
