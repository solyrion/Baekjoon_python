'''
k번째 최단경로 문제를 풀기위해 처음에 경로를 하나씩 지워가면서 경로를 저장하여 k번째 최단경로를 출력하였는데, 당연히 시간초과가 떴습니다.
구글링을 해본결과 이중배열 n X k를 생성해서 기본 다익스트라 알고리즘에서 최단거리를 갱신할때 k번째 길이와 비교후 sort를 해줍니다.
그러면 자연스럽게 1~k번째 최단거리를 구할 수 있게 됩니다.
'''

import sys, heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    ans[x][0] = 0
    while q:
        dis, ind = heapq.heappop(q)
        for i in d[ind]:
            tmp = i[1] + dis
            if tmp < ans[i[0]][k - 1]:
                ans[i[0]][k - 1] = tmp
                ans[i[0]].sort()
                heapq.heappush(q, (tmp, i[0]))

n, m, k = map(int, input().split())
d = [[] for _ in range(n+1)]
ans = [[inf]*k for _ in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    d[x].append([y, z])
    
dijkstra(1)

for i in range(1, n+1):
    if ans[i][k-1] == inf:
        print(-1)
    else:
        print(ans[i][k-1])
