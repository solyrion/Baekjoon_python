"""
각 대포내의 거리를 구한 후 50m기준으로 시간을 계산해야 합니다. 거리가 50m보다 작을 경우 (걸어가는 경우 / 50m를 2초에 대포로 날아간 후 남은 거리를 걸어가는 경우)로 나눠서 min값을
구해주고 50m보다 멀 경우 대포로 날아간 후 나머지 거리를 가는 시간을 계산하면 됩니다. 대포-대포 / 대포 - 도착점 간의 시간은 위와 같이 풀면 되지만 첫 출발점에서는 대포가 존재하지 않기
때문에 각 대포와 출발점 사이의 걸어가는데 걸리는 시간만을 구해야 합니다. 그 후에 dijkstra를 구하면 됩니다.
"""
import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def length(x1,y1,x2,y2, i, j):
    tmp = ((x1-x2)**2+(y1-y2)**2)**0.5
    if tmp > 50:
        k = 2 + (tmp - 50) / 5
    else:
        k = min(2+(50-tmp)/5, tmp/5)
    d[i].append([j, k])
    d[j].append([i, k])

def length2(x1,y1,x2,y2, i, j):
    tmp = ((x1-x2)**2+(y1-y2)**2)**0.5
    d[i].append([j, tmp/5])
    
def dijkstra(x):
    q = []
    l[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        dis, ind = heapq.heappop(q)
        if dis <= l[ind]:
            for i in d[ind]:
                tmp = dis + i[1]
                if tmp < l[i[0]]:
                    l[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))

x, y = map(float, input().split())
ax, ay =  map(float, input().split())
n = int(input())
t = [list(map(float, input().split())) for _ in range(n)]
d = [[] for _ in range(n+2)]

for i in range(n):
    a = t[i]
    length2(x,y,a[0],a[1],0, i+1)
    length(ax,ay,a[0],a[1],n+1, i+1)

for i in range(n):
    for j in range(i+1, n):
        a, b = t[i], t[j]
        length(a[0],a[1],b[0],b[1],i+1, j+1)
length2(x,y,ax,ay,0,n+1)

l = [inf]*(n+2)
dijkstra(0)
print(l[-1])
