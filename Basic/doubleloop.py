"""
중첩 반복문(2중 for문)
"""

# for i in range(5):
#     print("i:", i, sep="", end=" ")
#     for j in range(5):
#         print("j:", j, sep="", end=" ")
#     print()

# for i in range(5):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# for i in range(5):
#     for j in range(5, i, -1):
#         print("*", end=" ")
#     print()

for i in range(5):
    for j in range(5):
        if i > j:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

for i in range(5):
    for j in range(4, -1, -1):
        if i < j:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
