import sys

# sys.stdin = open("input.txt", "rt")

nums = [list(map(int, input().split())) for _ in range(9)]


def checkRow():
    for x in nums:
        smallList = list(set(x))
        if len(smallList) != 9:
            return False
    else:
        return True


def checkCols():
    cols = []
    for i in range(9):
        for j in range(9):
            cols.append(nums[j][i])

        cols = list(set(cols))
        if len(cols) != 9:
            return False
        cols.clear()
    else:
        return True


def checkSquare(start, end):
    sqaure = []
    for i in range(3):
        for j in range(3):
            sqaure.append(nums[i + start][j + end])

    sqaure = list(set(sqaure))
    if len(sqaure) != 9:
        return False
    sqaure.clear()
    return True


def solution():
    isFin = checkRow()
    if isFin:
        isFin = checkCols()

    if isFin:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                isFin = checkSquare(i, j)

    if isFin:
        print("YES")
    else:
        print("NO")


solution()
