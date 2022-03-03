import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp, t = [0] * n, []
dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i]+=1
x = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == x:
        x -= 1
        t.append(arr[i])
print(max(dp))
print(*t[::-1])