# 제일 작은 index를 출력하는 것이기 때문에 별도의 query함수 없이 1번째 node를 출력해주면 됩니다. 

import sys, math
input = sys.stdin.readline

def tree_make(node):
    if a[tree[node * 2]] <= a[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2]
    else:
        tree[node] = tree[node * 2 + 1]

def init(node, st, end):
    if st == end:
        tree[node] = st
    else:
        mid = (st + end) // 2
        init(node*2, st, mid)
        init(node*2 + 1, mid+1, end)
        tree_make(node)

def update(node, st, end, ind, val):
    if ind < st or ind > end:
        return
    if st == end:
        tree[node] = ind
        a[ind] = val
        return
    mid = (st + end) // 2
    update(node * 2, st, mid, ind, val)
    update(node * 2 + 1, mid + 1, end, ind, val)
    tree_make(node)

n = int(input())
a = list(map(int, input().split()))
tree = [0]*(1 << (math.ceil(math.log2(n))+1))
init(1, 0, n-1)
for _ in range(int(input())):
    x = list(map(int, input().split()))
    if x[0] == 1:
        update(1, 0, n-1, x[1]-1, x[2])
    else:
        print(tree[1]+1)
