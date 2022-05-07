import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def dfs():
    result = []
    q = deque()
    for i in range(1, n+1):
        if not ind[i]:
            q.append(i)
    while q:
        t = q.pop()
        result.append(t)
        for i in d[t]:
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)
    print(*result)

d = defaultdict(list)
n, m = map(int, input().split())
ind = [0]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    ind[y] += 1
    d[x].append(y)
dfs()
