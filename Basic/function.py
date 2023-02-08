"""
함수 만들기
"""
import math as m

# def add(a, b):
#     c = a + b
#     print(c)


# add(3, 2)
# add(5, 7)


# def add(a, b):
#     c = a + b
#     return c


# x = add(3, 2)
# print(x)


# def add(a, b):
#     c = a + b
#     d = a - b
#     return c, d  # 튜플 리턴


# print(add(1, 3))


def isPrime(x):
    num = int(m.sqrt(x))
    for i in range(2, num + 1):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]

for y in a:
    if isPrime(y):
        print(y, end=" ")
