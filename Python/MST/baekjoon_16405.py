"""
처음 e개의 집은 마을과 도보로 가능하다는 말은 구지 연결해줄 필요가 없다는 뜻입니다. 처리방법은 여러가지가 있겠지만 e > 1일 경우 서로 미리 u_parent를 해주면 됩니다.
그 후 p줄의 입력되는 마을은 서로 연결이 되어있으니 마찬가지로 입력되는 x,y에 대해 u_parent를 해주고 나머지에 대해 MST를 하면 됩니다.
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
        
n, e, p = map(int, input().split())
parent = [i for i in range(n+1)]
a = [list(map(float, input().split())) for _ in range(n)]
info = []

for _ in range(p):
    x, y = map(int, input().split())
    u_parent(x, y)

for i in range(n):
    for j in range(i+1, n):
        x, y = a[i],a[j]
        tmp = ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
        info.append((i+1, j+1, tmp))
info.sort(key = lambda x:x[2])

if e >= 2:
    for i in range(1, e):
        u_parent(i, i+1)
ans = 0
for x, y, z in info:
    if f_parent(x) != f_parent(y):
        u_parent(x, y)
        ans += z
print(ans)
