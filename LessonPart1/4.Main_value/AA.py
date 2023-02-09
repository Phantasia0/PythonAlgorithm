import sys

sys.stdin = open("input.txt", "rt")

N = int(input())
scores = list(map(int, input().split()))

avg = int(sum(scores) / len(scores) + 0.5)

min = float("inf")
students = []
for idx, score in enumerate(scores):
    standard = abs(score - avg)
    if standard < min:
        students.clear()
        min = standard
        students.append([score, idx])
    elif standard == min:
        students.append([score, idx])


students.sort(key=lambda v: (-v[0], v[1]))
print("{} {}".format(avg, students[0][1] + 1))
