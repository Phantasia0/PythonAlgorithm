import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
nums = list(map(int, input().split()))


def reverse(x):
    x = str(x)
    string = ""
    for i in range(len(x) - 1, -1, -1):
        string += x[i]

    string = int(string)
    return string


def isPrime(x):
    if x == 1:
        return False

    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


for num in nums:
    num = reverse(num)
    if isPrime(num):
        print(num, end=" ")
