"""
한번 이동시에 떡 하나만 들고 갈 수 있다는건 특정지점에 갔다가 돌아와야 하므로 최단거리*2만큼 이동해야 합니다.
최단거리를 구한 후 정렬합니다. 그리고 가장 거리가 먼 위치가 x보다 크다면 모든 지점에 대해 갈 수 없으므로 -1을 출력합니다.
"""
import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(k):
    di[k] = 0
    q = []
    heapq.heappush(q, (0, k))

    while q:
        dis, ind = heapq.heappop(q)
        if di[ind] >= dis:
            for i in d[ind]:
                tmp = i[1] + dis
                if tmp < di[i[0]]:
                    di[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))
    for i in range(n):
        if di[i] != inf: di[i] *= 2
        
n, m, x, y = map(int, input().split())
d = [[] for _ in range(n)]
di = [inf]*n

for i in range(m):
    a, b, c = map(int, input().split())
    d[a].append([b, c])
    d[b].append([a, c])
dijkstra(y)
di.sort()

if di[-1] > x:
    print(-1)
else:
    ans, tmp = 0, x
    for i in di:
        if i <= tmp:
            tmp -= i
        else:
            ans += 1
            tmp = x-i
    print(ans+1)
