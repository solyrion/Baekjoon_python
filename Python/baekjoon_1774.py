import sys
input = sys.stdin.readline

def f_parent(x):
    if x != parent[x]:
        parent[x] = f_parent(parent[x])
    return parent[x]

def u_parent(x, y):
    x = f_parent(x)
    y = f_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


m, n = map(int, input().split())
while m + n != 0:
    parent = [i for i in range(m)]
    info = []
    for i in range(n):
        info.append(list(map(int, input().split())))
    info = sorted(info, key=lambda x:x[2])
    ans = sum([i[2] for i in info])
    for i in range(n):
        x, y, z = info[i]
        if f_parent(x) != f_parent(y):
            ans -= z
            u_parent(x, y)
    print(ans)
    m, n = map(int, input().split())
