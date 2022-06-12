# 매 턴마다 범위내의 합을 출력하고 특정 index의 값을 바꿔주면되는 문제입니다.

import sys, math
input = sys.stdin.readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2 + 1]

def query(node, start, end, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    l_sum = query(node*2, start, (start+end)//2, left, right)
    r_sum = query(node*2 + 1, (start+end)//2 + 1,end, left, right)
    return l_sum + r_sum

def change(node, start, end, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
        a[index] = value
        return
    change(node*2, start, (start+end)//2, index, value)
    change(node*2+1, (start+end)//2+1, end, index, value)
    tree[node] = tree[node*2] + tree[node*2+1]

n, m = map(int, input().split())
a = list(map(int, input().split()))
tree = [0] * (1 << math.ceil(math.log2(n))+1)
init(a, tree, 1, 0, n - 1)

for i in range(m):
    k = list(map(int, input().split()))
    x, y = min(k[0],k[1]), max(k[0], k[1])
    print(query(1, 0, n-1, x-1, y-1))
    change(1, 0, n-1, k[2]-1, k[3])
