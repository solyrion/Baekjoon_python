"""
입력받은 a에서 a[i][j]<0 이면 u_parent를 해주고 값을 ans에 더해줍니다. 0보다 클 경우 info에 넣어주고 MST를 실행하면 됩니다.
"""
import sys
input = sys.stdin.readline

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

n = int(input())
parent = [i for i in range(n+1)]
a = [list(map(int, input().split())) for _ in range(n)]
info = []
ans = 0

for i in range(n):
    for j in range(i+1, n):
        if a[i][j] < 0:
            u_parent(i+1, j+1)
            ans += -a[i][j]
        else:
            info.append((i+1, j+1, a[i][j]))
info.sort(key = lambda x:x[2])

ct, k = 0, []
for x,y,z in info:
    if f_parent(x) != f_parent(y):
        u_parent(x, y)
        ans += z
        ct += 1
        k.append((x, y))
print(ans, ct)
for i in k:print(*i)
