"""
각 p개의 정점(y[i])에 대해 시작점(x) -> y[i] -> 도착점(z)를 구하면 됩니다. 다만 모든 y[i]에 대해 다익스트라를 하게되면 시간초과가 되기 때문에 역으로 z를 시작점으로 하는 다익스트라를 하면 됩니다.
그 후에 각 y[i]에 대해 (x->y[i])+(z->y[i])의 최소값을 구해주면 됩니다.
"""
import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(a):
    load = [inf]*(n+1)
    load[a] = 0
    q = []
    heapq.heappush(q, (0, a))
    while q:
        dis, ind = heapq.heappop(q)
        if dis <= load[ind]:
            for i in d[ind]:
                tmp = i[1] + dis
                if tmp < load[i[0]]:
                    load[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))
    return load

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append((y, z))
    d[y].append((x, z))
    
x, z = map(int, input().split())
pn = int(input())
p = list(map(int, input().split()))

a = dijkstra(x)
b = dijkstra(z)
ans = inf
for i in p:
    ans = min(ans, a[i]+b[i])

print(ans if ans < inf else -1)
