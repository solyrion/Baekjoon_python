"""
푸는데 오래걸리고 내용을 조금 참고했습니다. 문제의 큰 틀은 mst를 만든 후에 입력받은 x, y사이의 가장 비용이 큰 회선값을 mst값에서 뺴주면 됩니다.
x, y사이의 가장 비용이 큰 회선값은 bfs를 이용해서 구하면 됩니다.
"""
import sys, heapq
from collections import deque
input = sys.stdin.readline

def bfs(x):
    l[x][x] = 0
    q = deque()
    q.append((x, 0))
    while q:
        ind, ct = q.popleft()
        for a, b in d[ind]:
            if l[x][a] == -1:
                tmp = max(ct, b)
                l[x][a] = tmp
                q.append((a, tmp))

def f_parent(x):
    if x != parent[x]:
        parent[x] = f_parent(parent[x])
    return parent[x]

def u_parent(x, y):
    x, y = f_parent(x), f_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
d = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
info = []
l = [[-1]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(info, (z, x, y))
    
total = 0
while info:
    z, x, y = heapq.heappop(info)
    if f_parent(x) != f_parent(y):
        d[x].append([y, z])
        d[y].append([x, z])
        u_parent(x, y)
        total += z

for i in range(1, n+1):
    bfs(i)

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(total - l[x][y])
