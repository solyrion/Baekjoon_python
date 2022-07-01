# n-1위치를 제외하고 seeable이 1이라면 고려하지 않으면 됩니다. 다만 inf를 다른문제 풀 때 처럼 10**9정도면 부족하기에 좀더 늘려주었습니다.

import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**10+1

def dijkstra(x):
    q = []
    a[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        t, ind = heapq.heappop(q)
        if t > a[ind]:
            continue
        else:
            for i in d[ind]:
                if not seeable[i[0]] or i[0]==n-1:
                    if i[1] + t < a[i[0]]:
                        a[i[0]] = i[1] + t
                        heapq.heappush(q, (i[1] + t, i[0]))

n, m = map(int, input().split())
a = [inf]*n
d = defaultdict(list)
seeable = list(map(int, input().split()))
for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append((y, z))
    d[y].append((x, z))
    
dijkstra(0)
print(a[n-1] if a[n-1] != inf else -1)
