import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = 10**9+1

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    virus[x] = 0
    while q:
        v, ind = heapq.heappop(q)
        if v > virus[ind]:
            continue
        for i in dic[ind]:
            tmp = i[1] + v
            if tmp < virus[i[0]]:
                virus[i[0]] = tmp
                heapq.heappush(q, (tmp, i[0]))

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    dic = defaultdict(list)
    virus = [inf]*(n+1)

    for i in range(d):
        a, b, s = map(int, input().split())
        dic[b].append((a, s))
        
    dijkstra(c)
    ans = [i for i in virus if i != inf]
    print(len(ans), max(ans))
