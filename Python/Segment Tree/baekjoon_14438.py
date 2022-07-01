# 범위내의 최솟값, 특정 인덱스값 변경 두가지를 해결하는 문제입니다.

import sys, math
input = sys.stdin.readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node*2], tree[node*2 + 1])

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 10**9 + 1
    if left <= start and right >= end:
        return tree[node]
    l_min = query(tree, node * 2, start, (start + end) // 2, left, right)
    r_min = query(tree, node * 2+1, (start + end) // 2 + 1, end, left, right)
    return min(l_min, r_min)

def update(tree, a, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    update(tree, a, node*2, start, (start+end)//2, index, val)
    update(tree, a, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = min(tree[node*2], tree[node*2 + 1])

n = int(input())
a = list(map(int, input().split()))
tree = [0]*(1 << (math.ceil(math.log2(n))+1))
init(a, tree, 1, 0, n-1)

for i in range(int(input())):
    x, y, z = map(int, input().split())
    if x == 1:
        update(tree, a, 1, 0, n-1, y-1, z)
    else:
        print(query(tree, 1, 0, n-1, y-1, z-1))
