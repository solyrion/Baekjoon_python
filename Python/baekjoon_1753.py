import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**9

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, n = heapq.heappop(q)
        if dis < distance[n]:
            continue
        else:
            for i in d[n]:
                tmp = dis + i[1]
                if tmp < distance[i[0]]:
                    distance[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))


v, e = map(int, input().split())

k = int(input())
d = defaultdict(list)
distance = [inf]*(v+1)

for i in range(e):
    x, y, z = map(int, input().split())
    d[x].append((y, z))
dijkstra(k)

for i in range(1, v+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
