import sys, heapq
input = sys.stdin.readline
inf = 10**4

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    room[0][0] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        c, tx, ty = heapq.heappop(q)
        if c > room[tx][ty]:
            continue
        for i in range(4):
            cx, cy = dx[i]+tx, dy[i]+ty
            if 0<=cx<n and 0<=cy<n:
                tmp = abs(1-int(graph[tx][ty])) + room[tx][ty]
                if tmp < room[cx][cy]:
                    room[cx][cy] = tmp
                    heapq.heappush(q, (tmp, cx, cy))

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
room = [[inf]*n for _ in range(n)]
dijkstra()
print(room[-1][-1])
