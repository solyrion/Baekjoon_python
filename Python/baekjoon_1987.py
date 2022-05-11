import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    global max_
    max_ = max(max_, cnt)
    for i in range(4):
        tx, ty = x+dx[i], y+dy[i]
        if tx >= r or tx < 0 or ty >= c or ty < 0 or check[ord(graph[tx][ty])-65] != 0:
            continue
        else:
            check[ord(graph[tx][ty]) - 65] = 1
            dfs(tx, ty, cnt+1)
            check[ord(graph[tx][ty]) - 65] = 0

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
check = [0]*26
max_ = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check[ord(graph[0][0])-65] = 1
dfs(0, 0, 1)

print(max_)
