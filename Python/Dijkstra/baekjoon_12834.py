"""
각 팀원의 집 위치에서 KIST / 씨알푸드 위치 까지 최단거리를 구하면 됩니다. 최단거리가 inf와 같을경우 -1로 변경하고 두 최단거리를 더하면 됩니다.
"""
import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    while q:
        dis, ind = heapq.heappop(q)
        if dis <= distance[ind]:
            for i in d[ind]:
                tmp = i[1] + dis
                if tmp < distance[i[0]]:
                    distance[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))
    for i in [k, s]:
        if distance[i] == inf:
            distance[i] = -1
    return distance[k]+distance[s]

n, v, e = map(int, input().split())
k, s = map(int, input().split())
t = list(map(int, input().split()))
d = [[] for _ in range(v+1)]

for i in range(e):
    x, y, z = map(int, input().split())
    d[x].append([y, z])
    d[y].append([x, z])
ans = 0
for i in t:
    distance = [inf]*(v+1)
    distance[i] = 0
    ans += dijkstra(i)
print(ans)
