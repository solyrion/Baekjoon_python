"""
시작/도착 마을과 n개의 마을 총 n+2개의 마을에 대해 각 마을 간의 거리를 구하고 소수인 경우만 d에 저장해주고 dijkstra를 해주면 됩니다.
"""
import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

p = [1]*10**5
for i in range(2, len(p)):
    if p[i]:
        for j in range(i*i, len(p), i):
            p[j] = 0
p[0], p[1] = 0, 0

def dijkstra(x):
    dist[x] = 0
    q = []
    heapq.heappush(q, (0, x))
    while q:
        dis, ind = heapq.heappop(q)
        if dis <= dist[ind]:
            for i in d[ind]:
                tmp = i[1] + dis
                if tmp < dist[i[0]]:
                    dist[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))

x1, y1, x2, y2 = map(int, input().split())
n = int(input())
a = [[x1, y1]]
for _ in range(n):a.append(list(map(int, input().split())))
a.append([x2, y2])
d = [[] for _ in range(n+2)]

for i in range(n+2):
    for j in range(i+1, n+2):
        x, y = a[i], a[j]
        tmp = int(((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5)
        if p[tmp]:
            d[i].append([j, tmp])
            d[j].append([i, tmp])
            
dist = [inf]*(n+2)
dijkstra(0)
print(dist[n+1] if inf != dist[n+1] else -1)
