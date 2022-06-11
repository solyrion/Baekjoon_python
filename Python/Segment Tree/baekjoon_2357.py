# 기존 최솟값 문제에서 최댓값을 구하는게 추가된 문제입니다. 다만 최댓값또한 구해야하기 때문에 입력받은 a배열 원소를 음수로 저장한 b배열을 만든 후 tree2에 똑같이 세그멘트 트리를 이용해 구해줍니다.
# 음수로 저장했기에 최소로 구한 값에 '-'를 곱해준게 최댓값이 됩니다.

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

a = [int(input()) for _ in range(n)]
b = [-i for i in a]

tree = [0]*(1 << (math.ceil(math.log2(n))+1))
tree2 = [0]*(1 << (math.ceil(math.log2(n))+1))
init(a, tree, 1, 0, n-1)
init(b, tree2, 1, 0, n-1)

for i in range(m):
    x, y = map(int, input().split())
    print(query(tree, 1, 0, n-1, x-1, y-1), -query(tree2, 1, 0, n-1, x-1, y-1))
