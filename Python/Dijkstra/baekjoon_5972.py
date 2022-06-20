# 기본적인 다익스트라 문제입니다.
import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**9

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    food[x] = 0
    while q:
        f, ind = heapq.heappop(q)
        if food[ind] < f:
            continue
        for i in d[ind]:
            tmp = f + i[1]
            if tmp < food[i[0]]:
                food[i[0]] = tmp
                heapq.heappush(q, (tmp, i[0]))

n, m = map(int, input().split())
d = defaultdict(list)
food = [inf] * (n+1)
for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append((y, z))
    d[y].append((x, z))
    
dijkstra(1)
print(food[n])
