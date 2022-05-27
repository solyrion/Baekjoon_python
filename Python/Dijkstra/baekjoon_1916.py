import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**9

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    price[start] = 0
    while q:
        dis, n = heapq.heappop(q)
        if dis > price[n]:
            continue
        else:
            for i in d[n]:
                tmp = dis + i[1]
                if tmp < price[i[0]]:
                    price[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))

n = int(input())
m = int(input())
d = defaultdict(list)
price = [inf]*(n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append((y, z))

s, e = map(int, input().split())
dijkstra(s)
print(price[e])
