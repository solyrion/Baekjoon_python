import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def dfs():
    q = deque()
    for i in range(1, n+1):
        if not ind[i]:
            q.append(i)
            ct[i][i] = 1
    while q:
        t = q.pop()
        for i in d[t]:
            ind[i[0]] -= 1
            for j in ct[t]:
                ct[i[0]][j] += ct[t][j]*i[1]
            if not ind[i[0]]:
                q.append(i[0])

n = int(input())
ind = [0]*(n+1)
ct = [defaultdict(int) for _ in range(n+1)]
d = defaultdict(list)

for i in range(int(input())):
    x, y, k = map(int, input().split())
    d[y].append((x, k))
    ind[x] += 1
dfs()

for i in sorted(list(ct[n].keys())):
    print(i, ct[n][i])
