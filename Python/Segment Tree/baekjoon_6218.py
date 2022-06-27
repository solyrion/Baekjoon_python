# 기존의 세그트리를 이용한 최대최소문제와 같습니다. 그러나 이전에 제가 푼 tree를 2개 선언하여 푸는것이 아닌 tree의 각 node를 [min, max]로 두고 풀었습니다.

import sys, math
input = sys.stdin.readline

def init(node, st, end):
    if st == end:
        tree[node] = [a[st], a[st]]
    else:
        mid = (st+end) // 2
        init(node * 2, st, mid)
        init(node * 2 + 1, mid+1, end)
        tree[node][0] = min(tree[node*2][0], tree[node*2+1][0])
        tree[node][1] = max(tree[node*2][1], tree[node*2+1][1])

def query(node, st, end, l, r):
    if l <= st and end <= r:
        return tree[node]
    if l > end or r < st:
        return [10**7, 0]
    mid = (st+end)//2
    l_q = query(node*2, st, mid, l, r)
    r_q = query(node*2+1, mid+1, end, l, r)

    return [min(l_q[0], r_q[0]), max(l_q[1], r_q[1])]


n, q = map(int, input().split())
a = [int(input()) for i in range(n)]
tree = [[0, 0] for _ in range(1 << (math.ceil(math.log2(n))+1))]
init(1, 0, n-1)
for i in range(q):
    x, y = map(int, input().split())
    k = query(1, 0, n-1, x-1, y-1)
    print(k[1]-k[0])
