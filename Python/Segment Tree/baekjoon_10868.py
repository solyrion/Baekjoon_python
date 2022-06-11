# 기존 구간합 문제와 비슷합니다. 다만 Update과정이 없고 init과 query함수 내부에서 tree갱신과정에서 min()을 이용해 최솟값을 저장해줍니다.


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


n, m = map(int, input().split())
a = [int(input()) for i in range(n)]

tree = [0]*(1 << (math.ceil(math.log2(n))+1))
init(a, tree, 1, 0, n-1)
for i in range(m):
    x, y = map(int, input().split())
    print(query(tree, 1, 0, n-1, x-1, y-1))
