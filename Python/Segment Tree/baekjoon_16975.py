"""
구간 합 구하기 2랑 같은 문제입니다. 다만 범위의 합이 아닌 변경된 배열의 특정 index의 값을 출력하는 문제입니다. 아래 코드에서 처음 입력받은 배열 a값을 변경하지는 않기 때문에,
query 함수에서 x를 기준으로 해서 tree내에서 st==end==x인 node를 찾으면 됩니다.
"""
import sys, math
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start+end)//2
        init(node*2, start, mid)
        init(node*2 + 1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2 + 1] += lazy[node]
        lazy[node] = 0

def update_range(node, start, end, left, right, diff):
    update_lazy(node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end-start+1)*diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2 + 1] += diff
        return
    mid = (start + end) // 2
    update_range(node*2, start, mid, left, right, diff)
    update_range(node*2+1, mid+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2 + 1]

def query(node, start, end, x):
    update_lazy(node, start, end)
    if x < start or x > end:
        return 0
    if start == x and end == x:
        return tree[node]
    else:
        mid = (start + end) // 2
        l = query(node * 2, start, mid, x)
        r = query(node * 2 + 1, mid + 1, end, x)
        return l + r

n = int(input())
a = list(map(int, input().split()))
h = math.ceil(math.log2(n))+1
tree = [0]*(1 << h)
lazy = [0]*(1 << h)
init(1, 0, n-1)

for i in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        left, right, diff = q[1:]
        update_range(1, 0, n-1, left-1, right-1, diff)
    else:
        x = q[1]
        print(query(1, 0, n-1, x-1))
