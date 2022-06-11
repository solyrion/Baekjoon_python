# 기존 구간합 문제와 같다. 다만 합이 아닌 곱이기에 코드의 모든 갱신부분에서 + 대신 *을 써야한다.

import sys, math
input = sys.stdin.readline
num = 1000000007

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = (tree[node*2] * tree[node*2 + 1]) % num

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]
    l = query(tree, node * 2, start, (start + end) // 2, left, right)
    r = query(tree, node * 2+1, (start + end) // 2 + 1, end, left, right)
    return (l*r) % num

def update(tree, a, node, start, end, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
        a[start] = value
        return
    update(tree, a, node*2, start, (start+end)//2, index, value)
    update(tree, a, node*2 + 1, (start+end)//2+1, end, index, value)
    tree[node] = (tree[node*2] * tree[node*2 + 1])%num

n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

tree = [0]*(1 << (math.ceil(math.log2(n))+1))
init(a, tree, 1, 0, n-1)

for i in range(m+k):
    x, y, z = map(int, input().split())
    if x == 1:
        update(tree, a, 1, 0, n-1, y-1, z)
    else:
        print(query(tree, 1, 0, n-1, y-1, z-1))
