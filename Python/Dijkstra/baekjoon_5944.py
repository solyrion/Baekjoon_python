"""
pb->pa1->pa2 / pb->pa2->pa1 의 최단거리중 최소값을 출력하면 됩니다.
"""
import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(x, vp):
    vp[x] = 0
    q = []
    heapq.heappush(q, (0, x))
    while q:
        dis, ind = heapq.heappop(q)
        if dis <= vp[ind]:
            for i in d[ind]:
                tmp = i[1] + dis
                if tmp < vp[i[0]]:
                    vp[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))
    return vp

c, p, pb, pa1, pa2 = map(int, input().split())
d = [[] for _ in range(p+1)]

for _ in range(c):
    x, y, z = map(int, input().split())
    d[x].append([y, z])
    d[y].append([x, z])

vp = [inf]*(p+1)
vpa1, vpa2 = [inf]*(p+1), [inf]*(p+1)
vp, vpa1, vpa2 = dijkstra(pb, vp), dijkstra(pa1, vpa1), dijkstra(pa2, vpa2)
print(min(vp[pa1]+vpa1[pa2], vp[pa2]+vpa2[pa1]))
