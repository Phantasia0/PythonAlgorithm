"""
리스트와 내장함수
"""
import random as r

# a= []
# print(a)
# b=list()
# print(b)

a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])

b = list(range(1, 11))
# print(b)

c = a + b
# print(c)

a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)

a.pop(3)
print(a)

a.remove(4)
print(a)

print(a.index(5))  # 값이 5인 인덱스 출력

a = list(range(1, 11))
print(a)
print(sum(a))
print(max(a))
print(min(a))
print(min(7, 5))  # 인자 값들 중 최소 7,5중 최소
print(min(7, 3, 5))
print(a)

r.shuffle(a)
print(a)

a.sort(reverse=True)  # 내림차순
print(a)

a.sort()  # 오름차순
print(a)

a.clear()
print(a)

# tuple_list = [
#     ("좋은하루", 0),
#     ("niceday", 1),
#     ("좋은하루", 5),
#     ("good_morning", 3),
#     ("niceday", 5),
# ]

# tuple_list.sort(key=lambda x: -x[1])
# print(tuple_list)

# tuple_list.sort(key=lambda x: x[1])
# print(tuple_list)

# array = [
#     ("A", 18, 300000),
#     ("F", 24, 10000),
#     ("T", 24, 200000),
#     ("Q", 24, 5000000),
#     ("B", 70, 5000),
# ]

# array.sort(key=lambda x: (x[1], -x[2]))
# print(array)

a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=" ")
print()

for x in a:
    print(x, end=" ")
print()

for x in a:
    if x % 2 == 1:
        print(x, end=" ")
print()

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(50 > x for x in a):
    print("YES")
else:
    print("NO")

if any(15 > x for x in a):
    print("YES")
else:
    print("NO")
