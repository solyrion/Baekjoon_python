"""
1~N 각각을 출발점으로 하여 다익스트라를 하면 됩니다. 최종 거리가 INF인 경우 도달할 수 없는 곳이기 때문에 0으로 변경 후 출력하면 됩니다.
"""

import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(x):
    q = []
    c = [inf]*(n+1)
    c[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        dis, ind = heapq.heappop(q)
        if dis <= c[ind]:
            for i in d[ind]:
                tmp = i[1] + dis
                if tmp < c[i[0]]:
                    c[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))
    return c

n = int(input())
m = int(input())
d = [[] for _ in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append((y, z))
    
for i in range(1, n+1):
    k = dijkstra(i)
    for i in range(1, n+1):
        if k[i] == inf:k[i] = 0
    print(*k[1:])
