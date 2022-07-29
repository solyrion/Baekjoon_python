"""
모든 맥도날드, 스타벅스 매장에 대해 다익스트라를 이용해서 문제를 풀 수는 있지만 시간초과에 걸리게 됩니다. MST문제를 전에 풀던중 배운것이 있는데 새로운 node를 하나 생성하는것입니다.
모든 맥도날드를 n+1번 node와 거리 0으로 엮고, 스타벅스는 n+2번 node와 엮습니다. 그 후에 n+1 / n+2 node에 대해 입력으로 주어진 거리조건에 맞추어 해결하면 됩니다.
"""
import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(x, y):
    q = []
    info = [y+1] * (n+3)
    info[x] = 0
    heapq.heappush(q, (0, x))

    while q:
        dis, ind = heapq.heappop(q)
        if info[ind] >= dis:
            for i in d[ind]:
                tmp = i[1] + dis
                if tmp < info[i[0]]:
                    info[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))
    return info

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(m):
    x, y, z = map(int,input().split())
    d[x].append((y, z))
    d[y].append((x, z))

m, mx = map(int, input().split())
ml = list(map(int, input().split()))
s, sx = map(int, input().split())
sl = list(map(int, input().split()))

dm, ds = n+1, n+2
for i in ml:d[dm].append((i, 0))
for i in sl:d[ds].append((i, 0))

info_m = dijkstra(dm, mx)
info_s = dijkstra(ds, sx)

ans = mx+sx+2

for i in range(1, n+1):
    if not(i in sl or i in ml):
        x, y = info_m[i], info_s[i]
        if x < mx+1 and y < sx+1:
            ans = min(ans, x+y)
            
print(ans if ans != mx+sx+2 else -1)
