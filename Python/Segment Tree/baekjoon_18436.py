# 각 트리를 [0, 0]배열로 두고 짝수와 홀수의 개수를 더해줬습니다. 처음 제출에 틀려서 고쳤던 부분은 update과정에서 홀짝 판별이후 나머지 부분 (홀수면 짝수 짝수면 홀수)을 0으로 바꿔줘야한다는 것입니다.
# 왜냐하면 기존수가 짝수고 바뀐수가 홀수일때 나머지 부분을 바꿔주지 않는다면 [1, 1]이 될 수 도 있기 때문입니다.
import sys, math
input = sys.stdin.readline

def init(node, st, end):
    if st == end:
        if a[st] % 2 == 0:
            tree[node][0] = 1
        else:
            tree[node][1] = 1
    else:
        mid = (st+end)//2
        init(node*2, st, mid)
        init(node*2+1, mid+1, end)
        for i in range(2):
            tree[node][i] = tree[node*2][i] + tree[node*2+1][i]

def query(node, st, end, l, r):
    if l > end or r < st:
        return [0, 0]
    if l <= st and end <= r:
        return tree[node]
    mid = (st+end)//2
    l_c = query(node*2, st, mid, l, r)
    r_c = query(node*2 + 1, mid+1, end, l, r)
    return [l_c[0]+r_c[0], l_c[1]+r_c[1]]

def update(node, st, end, ind, val):
    if ind < st or ind > end:
        return
    if st == end:
        a[st] = val
        tree[node] = [0, 0]
        if val % 2 == 0:
            tree[node][0] = 1
        else:
            tree[node][1] = 1
        return
    mid = (st + end)//2
    update(node*2, st, mid, ind, val)
    update(node*2+1, mid+1, end, ind, val)
    for i in range(2):
        tree[node][i] = tree[node*2][i] + tree[node*2+1][i]
    
n = int(input())
a = list(map(int, input().split()))
tree = [[0,0] for _ in range(1 << (math.ceil(math.log2(n))+1))]
init(1, 0, n-1)
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if x == 1:
        update(1, 0, n-1, y-1, z)
    else:
        ans = query(1, 0, n-1, y-1, z-1)
        if x == 2:
            print(ans[0])
        else:
            print(ans[1])
