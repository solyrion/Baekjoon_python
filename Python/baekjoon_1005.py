import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def solve():
    q = deque()
    for i in range(1, n+1):
        if not ind[i]:
            q.append(i)
            time[i-1] = t[i-1]

    while q:
        x = q.pop()
        for i in d[x]:
            ind[i] -= 1
            time[i-1] = max(time[i-1], time[x-1])
            if not ind[i]:
                q.append(i)
                time[i-1] += t[i-1]

for _ in range(int(input())):
    n, k = map(int, input().split())
    t = list(map(int, input().split()))
    d = defaultdict(list)
    ind = [0]*(n+1)
    time = [0]*(n+1)

    for i in range(k):
        x, y = map(int, input().split())
        d[x].append(y)
        ind[y] += 1
        
    w = int(input())
    
    solve()
    print(time[w-1])
