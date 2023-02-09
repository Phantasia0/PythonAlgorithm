import sys

# sys.stdin = open("input.txt", "r")

cards = []
for i in range(21):
    cards.append(i)

for i in range(10):
    start, end = map(int, input().split())
    if (start - end) % 2 == 0:
        for i in range(start, int((start + end) / 2)):
            cards[i], cards[end - (i - start)] = cards[end - (i - start)], cards[i]
    else:
        for i in range(start, int((start + end) / 2) + 1):
            cards[i], cards[end - (i - start)] = cards[end - (i - start)], cards[i]

for i in range(1, 21):
    print(cards[i], end=" ")
