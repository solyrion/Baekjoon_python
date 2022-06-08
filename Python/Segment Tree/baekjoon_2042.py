import sys, math
input = sys.stdin.readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2 + 1]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    l_sum = query(tree, node * 2, start, (start + end) // 2, left, right)
    r_sum = query(tree, node * 2+1, (start + end) // 2 + 1, end, left, right)
    return l_sum + r_sum

def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    update(a, tree, node * 2, start, (start + end) // 2, index, val)
    update(a, tree, node * 2 + 1, (start + end) // 2 + 1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2 + 1]

n, m, k = map(int, input().split())
a = [int(input()) for i in range(n)]
tree = [0]*(1 << (math.ceil(math.log2(n))+1))
init(a, tree, 1, 0, n-1)

for i in range(m+k):
    x, y, z = map(int, input().split())
    if x == 2:
        print(query(tree, 1, 0, n-1, y-1, z-1))
    else:
        update(a, tree, 1, 0, n-1, y-1, z)
       
      
      
# 첫 세그먼트 트리문제, 어려운 개념이기에 추가적인 공부(이해)필요함
