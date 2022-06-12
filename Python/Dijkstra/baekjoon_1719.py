import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    distance = [10**8]*(n+1)
    distance[x] = 0
    ans[x][x] = '-'
    while q:
        dis, ind = heapq.heappop(q)
        if distance[ind] < dis:
            continue
        for i in d[ind]:
            tmp = i[1] + dis
            if tmp < distance[i[0]]:
                distance[i[0]] = tmp
                heapq.heappush(q, (tmp, i[0]))
                if ans[x][ind] == '-':
                    ans[x][i[0]] = i[0]
                else:
                    ans[x][i[0]] = ans[x][ind]

n, m = map(int, input().split())
d = defaultdict(list)
ans = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append((y, z))
    d[y].append((x, z))
    
for i in range(1, n+1):
    dijkstra(i)

for i in range(1, n+1):
    print(*ans[i][1:])
