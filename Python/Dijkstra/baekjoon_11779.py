import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**8+1

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    price[x] = 0
    load[x].append(x)

    while q:
        p, l = heapq.heappop(q)
        if p > price[l]:
            continue
        else:
            for i in d[l]:
                tmp = p + i[1]
                if tmp < price[i[0]]:
                    load[i[0]] = load[l][:]
                    load[i[0]].append(i[0])
                    price[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))

n = int(input())
m = int(input())
d = defaultdict(list)
price = [inf]*(n+1)
load = [[] for _ in range(n+1)]

for i in range(m):
    x, y, c = map(int, input().split())
    d[x].append((y, c))
x, y = map(int, input().split())
dijkstra(x)

print(price[y])
print(len(load[y]))
print(*load[y])
