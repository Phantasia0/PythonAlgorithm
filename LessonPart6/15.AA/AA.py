import sys

sys.stdin = open("input.txt", "rt")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m, n = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = 0
count = 0
isNotCompleted = False

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            cnt += 1
previous = 0
if cnt == 0:
    print(0)
    sys.exit(0)
else:
    while True:
        previous = cnt
        cnt = 0
        check = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if box[i][j] == 1 and check[i][j] == 0:
                    check[i][j] = 1
                    box[i][j] = -1
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0 <= x < n and 0 <= y < m:
                            if box[x][y] == 0:
                                if check[x][y] == 0:
                                    box[x][y] = 1
                                    check[x][y] = 1
        count += 1
        for i in range(n):
            cnt += box[i].count(0)

        if cnt == 0:
            break
        if previous == cnt:
            isNotCompleted = True
            break


if isNotCompleted:
    print(-1)
else:
    print(count)
