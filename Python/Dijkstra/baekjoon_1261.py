import sys, heapq
input = sys.stdin.readline
inf = 10**5

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    wall[x][y] = 0
    while q:
        t = heapq.heappop(q)
        for i in range(4):
            tx, ty = dx[i]+t[1], dy[i]+t[2]
            if 0 <= tx < n and 0 <= ty < m:
                if t[0] > wall[tx][ty]:
                    continue
                else:
                    tmp = graph[tx][ty] + t[0]
                    if tmp < wall[tx][ty]:
                        wall[tx][ty] = tmp
                        heapq.heappush(q, (tmp, tx, ty))

m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
wall = [[inf]*m for _ in range(n)]
dijkstra(0, 0)

print(wall[n-1][m-1])
