import sys

sys.stdin = open("input.txt", "rt")

testCase = int(input())


# for i in range(1, testCase + 1):
#     N, s, e, k = map(int, input().split())
#     numbers = list(map(int, input().split()))
#     result = []
#     cnt = 0
#     for j in range(len(numbers)):
#         cnt += 1
#         if s - 1 <= cnt < e:
#             result.append(numbers[cnt])
#         elif cnt >= e:
#             break
#     result.sort()
#     print("{}{} {}".format("#", i, result[k - 1]))

for i in range(1, testCase + 1):
    N, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    # numbers = [int(x) for x in input().split()]

    numbers = numbers[s - 1 : e]
    numbers.sort()
    # print("{}{} {}".format("#", i, numbers[k - 1]))
    # print("#%d %d" % (i, numbers[k - 1]))
