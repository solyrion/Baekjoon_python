import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**5

def dijkstra(x):
    min_dis = [inf]*(n+1)
    q = []
    min_dis[x] = 0
    heapq.heappush(q, (0, x))

    while q:
        dis, ind = heapq.heappop(q)
        if min_dis[ind] < dis:
            continue
        for i in d[ind]:
            tmp = i[1] + dis
            if tmp < min_dis[i[0]]:
                min_dis[i[0]] = tmp
                heapq.heappush(q, (tmp, i[0]))
    for i in range(1, n+1):
        if min_dis[i] <= m:
            p_item[x-1] += item[i-1]

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
p_item = [0]*n
d = defaultdict(list)

for i in range(r):
    x, y, z = map(int, input().split())
    d[x].append((y, z))
    d[y].append((x, z))
    
for i in range(1, n+1):
    dijkstra(i)
print(max(p_item))
