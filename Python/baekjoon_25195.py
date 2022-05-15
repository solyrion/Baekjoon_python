import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x):
    if not d[x]:
        print("yes")
        exit()
    visit[x] = 1
    for i in d[x]:
        if not visit[i]:
            if i not in arr:
                dfs(i)

d = defaultdict(list)
n, m = map(int, input().split())

for i in range(m):
    x, y = map(int, input().split())
    d[x].append(y)
    
s = int(input())
arr = list(map(int, input().split()))
visit = [0] * (n + 1)

if 1 not in arr:
    dfs(1)
    
print("Yes")
