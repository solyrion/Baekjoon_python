import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**9

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dis, n = heapq.heappop(q)
        if dis > distance[n]:
            continue
        else:
            for i in d[n]:
                tmp = dis + i[1]
                if tmp < distance[i[0]]:
                    distance[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))

n, m, s = map(int, input().split())
d = defaultdict(list)
distance_all = [[inf]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append((y, z))

for i in range(1, n+1):
    dijkstra(i, distance_all[i])

print(max([distance_all[s][i] + distance_all[i][s] for i in range(1, n+1)]))
