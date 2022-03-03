import sys
input = sys.stdin.readline

def check(n):
    for i in range(len(p)):
        for j in range(i, len(p)):
            if p[i] + p[j] == n:
                total.extend([p[i],p[j]])
                return

k = 1100000
p = [0,0,1]+[1]*k
for i in range(2, len(p)):
    if p[i]:
        for j in range(i*2, len(p), i):
            p[j] = 0
p = [i for i in range(2, len(p)) if p[i]]
n = int(input())
if n < 8:print(-1)
else:
    if n % 2 == 0:
        total, n = [2, 2], n - 4
    else:
        total, n = [2, 3], n - 5
    check(n)
    print(*total)