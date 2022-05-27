import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**9

def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])

    while q:
        dis, ind = heapq.heappop(q)
        if distance[ind] < dis:
            continue
        else:
            for i in d[ind]:
                tmp = dis + i[1]
                if tmp < distance[i[0]]:
                    distance[i[0]] = tmp
                    heapq.heappush(q, [tmp, i[0]])

n, e = map(int, input().split())

dis1 = [inf]*(n+1)
dis2 = [inf]*(n+1)
dis3 = [inf]*(n+1)
d = defaultdict(list)

for i in range(e):
    x, y, z = map(int, input().split())
    d[x].append((y, z))
    d[y].append((x, z))
    
v1, v2 = map(int, input().split())

dijkstra(1, dis1)
dijkstra(v1, dis2)
dijkstra(v2, dis3)

ans1 = dis1[v1] + dis2[v2] + dis3[n]
ans2 = dis1[v2] + dis3[v1] + dis2[n]
ans = min(ans1, ans2)

print(ans if ans < inf else -1)
