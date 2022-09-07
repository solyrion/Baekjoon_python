"""
새롭게 배운 알고리즘입니다. 기존의 세그멘트 트리는 크기가 큰 배열의 많은 횟수의 쿼리를 수행하는데 효과적이였지만, 이번 문제와 같이 쿼리가 특정 위치의 숫자만이 아닌 특정 범위의 숫자를 변경하는 경우
기존의 세그멘트 트리로는 제한시간 내에 해결할 수 없습니다. 그래서 배우게 된 알고리즘이 느리게 갱신되는 세그멘트 트리입니다. diff(더해줘야 하는 수)를 저장해주는 방식입니다. lazy 트리를 생성해서
해당 node에 diff값을 저장해줍니다. tree에 갱신할때는 (end-start+1)*diff 만큼 더해줍니다.
취지는 각 쿼리 범위를 매번 바꿔주는것이 아닌 저장해놓고 다시 접근할때 갱신해주는 방식입니다.
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

def query(node, start, end, left, right):
    update_lazy(node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end) // 2
    lsum = query(node*2, start, mid, left, right)
    rsum = query(node*2+1, mid+1, end, left, right)
    return lsum+rsum

n, m, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))+1
tree = [0]*(1 << h)
lazy = [0]*(1 << h)
init(1, 0, n-1)

for i in range(m+k):
    q = list(map(int, input().split()))
    if q[0] == 1:
        left, right, diff = q[1:]
        update_range(1, 0, n-1, left-1, right-1, diff)
    else:
        left, right = q[1:]
        print(query(1, 0, n-1, left-1, right-1))
