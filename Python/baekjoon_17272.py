import sys
input = sys.stdin.readline
p = 1000000007

def pow(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        return pow(multi(matrix, matrix), n // 2)
    else:
        return multi(pow(matrix, n-1), matrix)

def multi(a, b):
    tmp = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            sum_ = 0
            for k in range(m):
                sum_ += a[i][k] * b[k][j]
            tmp[i][j] = sum_ % p
    return tmp

n, m = map(int, input().split())

first = [[0]*m for _ in range(m)]
first[0][0], first[0][m-1] = 1, 1
for i in range(1, m):
    first[i][i-1] = 1

print(pow(first, n)[0][0])
