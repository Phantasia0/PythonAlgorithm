import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")

heap = []

while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        if heap:
            print(hq.heappop(heap))
        else:
            print(-1)
    else:
        hq.heappush(heap, num)
