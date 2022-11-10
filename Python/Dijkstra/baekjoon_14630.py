"""
각 변신상태를 기준으로 다른 변신상태와의 비용을 계산 후에 다익스트라 알고리즘을 구현하면 됩니다.
"""
import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def calc(x, y):
    ans = 0
    for i in range(len(x)):
        ans += (int(x[i])-int(y[i]))**2
    return ans

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    v[x] = 0
    while q:
        ct, ind = heapq.heappop(q)
        if ct <= v[ind]:
            for i in d[ind]:
                tmp = i[1]+ct
                if tmp < v[i[0]]:
                    v[i[0]] = tmp
                    heapq.heappush(q, (tmp, i[0]))

n = int(input())
d = [[] for _ in range(n+1)]
a = [input().strip() for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        t = calc(a[i], a[j])
        d[i+1].append([j+1, t])
        d[j+1].append([i+1, t])

v = [inf]*(n+1)
x, y = map(int, input().split())
dijkstra(x)
print(v[y])
