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
    tmp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum_ = 0
            for k in range(2):
                sum_ += a[i][k] * b[k][j]
            tmp[i][j] = sum_ % p
    return tmp


first = [[1, 1],[1, 0]]
s_mul = [[1], [1]]

n = int(input())
if n < 3:
    print(1)
else:
    print(multi(pow(first, n-2), s_mul)[0][0])
