"""
x->y->z 와 x->z의 최단경로를 출력하면 됩니다. 다만 x->z의 최단경로를 구하는 과정에서 y를 지나올 수 있기 때문에 별도의 k를 함수의 인자로 받아서 k == 1일경우(x->z를 구하는경우)
y를 생략하는 과정이 필요합니다.
"""
import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
inf = sys.maxsize 

def dijkstra(a, b, k):
    load = [inf]*(n+1)
    load[a] = 0

    q = []
    heapq.heappush(q, (0, a))
    while q:
        dis, ind = heapq.heappop(q)
        if dis <= load[ind]:
            for i in d[ind]:
                if i[0] == y and k:
                    continue
                tmp = i[1] + dis
                if tmp < load[i[0]]:
                    load[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))
    return load[b]

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append((y, z))

x, y, z = map(int ,input().split())
ans = [dijkstra(x, y, 0)+dijkstra(y, z, 0), dijkstra(x, z, 1)]
for i in range(2):
    if ans[i] >= inf:ans[i] = -1
print(*ans)
