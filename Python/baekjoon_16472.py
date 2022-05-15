
import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().strip())
s, f = 0, 1

if len(arr) == 1:
  print(1)
else:
    m, w = -1, {arr[s]}
    while f < len(arr):
        w.add(arr[f])
        if len(w) <= n:
            m = max(m, f-s+1)
            f += 1
        else:
            s += 1
            w = set(arr[s:f+1])
    print(m)
