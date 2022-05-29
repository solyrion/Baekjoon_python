import sys, heapq
input = sys.stdin.readline
inf = 10**6

def dijkstra():
    coin[0][0] = graph[0][0]
    q = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    heapq.heappush(q, (coin[0][0], 0, 0))

    while q:
        c, x, y = heapq.heappop(q)
        if c > coin[x][y]:
            continue
        else:
            for i in range(4):
                tx, ty = dx[i]+x, dy[i]+y
                if 0 <= tx < n and 0 <= ty < n:
                    tmp = c + graph[tx][ty]
                    if tmp < coin[tx][ty]:
                        coin[tx][ty] = tmp
                        heapq.heappush(q, (tmp, tx, ty))

n = int(input())
ct = 1
while n:
    graph = [list(map(int, input().split())) for _ in range(n)]
    coin = [[inf]*n for _ in range(n)]
    dijkstra()
    print("Problem %d: %d"%(ct, coin[n-1][n-1]))
    n = int(input())
    ct += 1
