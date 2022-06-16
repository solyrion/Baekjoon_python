# 처음에는 모두 0이기 때문에 init함수는 필요하지 않습니다. update함수에서는 tree[node]에 계속 더해주면 됩니다.
import sys, math
input = sys.stdin.readline

def query(node, st, end, p, q):
    if p <= st and q >= end:
        return tree[node]
    if p > end or q < st:
        return 0
    mid = (st + end) // 2
    l = query(node*2, st, mid, p, q)
    r = query(node*2 + 1, mid+1, end, p, q)
    return l + r

def update(node, st, end, ind, val):
    if ind < st or ind > end:
        return
    if st == end:
        tree[node] += val
        return
    mid = (st + end) // 2
    update(node*2, st, mid, ind, val)
    update(node*2+1, mid+1, end, ind, val)
    tree[node] = tree[node*2] + tree[node*2 + 1]
    
n, m = map(int, input().split())
tree = [0]*(1 << (math.ceil(math.log2(n))+1))

for i in range(m):
    x, y, z = map(int, input().split())
    if x == 1:
        update(1, 0, n-1, y-1, z)
    else:
        print(query(1, 0, n-1, y-1, z-1))
