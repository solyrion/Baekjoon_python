# 기존 구간 곱 구하기 문제랑 같습니다만, 그 문제와는 다르게 나눌 특정수가 없기에 숫자가 매우 커질 수 있습니다. 이 문제는 결국 '+' / '-' / 0 즉 부호만 판별하면 되기 때문에 트리에 각 배열 index의
# 부호에 따른 1 / -1 / 0를 넣어 해결합니다.

import sys, math
input = sys.stdin.readline

def init(node, st, end):
    if st == end:
        if a[st] < 0:tree[node] = -1
        elif a[st] > 0:tree[node] = 1
        else: tree[node] = 0
    else:
        t = (st+end)//2
        init(node*2, st, t)
        init(node*2+1, t+1, end)
        tree[node] = tree[node*2] * tree[node*2 + 1]

def query(node, st, end, l, r):
    if l <= st and r >= end:
        return tree[node]
    if st > r or end < l:
        return 1
    t = (st+end)//2
    l_c = query(node * 2, st, t, l, r)
    r_c = query(node * 2 + 1, t + 1, end, l, r)
    return l_c * r_c

def change(node, st, end, ind, val):
    if ind < st or ind > end:
        return
    if st == end:
        a[ind] = val
        if val < 0:tree[node] = -1
        elif val > 0:tree[node] = 1
        else:tree[node] = 0
        return
    t = (st + end) // 2
    change(node * 2, st, t, ind, val)
    change(node * 2 + 1, t + 1, end, ind, val)
    tree[node] = tree[node*2] * tree[node*2 + 1]

while True:
    try:
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        tree = [0] * (1 << (math.ceil(math.log2(n))+1))
        init(1, 0, n-1)
        ans = ""
        for i in range(m):
            q = input().split()
            if q[0] == 'C':
                change(1, 0, n - 1, int(q[1]) - 1, int(q[2]))
            else:
                k = query(1, 0, n - 1, int(q[1]) - 1, int(q[2]) - 1)
                if k > 0:
                    ans += '+'
                elif k < 0:
                    ans += '-'
                else:
                    ans += '0'
        print(ans)
    except:
        break
