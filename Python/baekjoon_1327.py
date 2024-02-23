import sys, heapq
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(input().split())
v = set("".join(a))
total = sorted(a)
q = deque([(a, 0)])
ans = -1

while q:
    arr, ct = q.popleft()
    if arr == total:
        ans = ct
        break
    for i in range(n-k+1):
        tmp = arr[i:i+k]
        tmp.reverse()
        tmp = arr[:i] + tmp + arr[i+k:]
        stmp = "".join(tmp)
        if stmp not in v:
            v.add(stmp)
            q.append((tmp, ct + 1))
          
print(ans)

"""
처음 보고 그래프를 떠올리기는 어려웠습니다. 일반적으로 그래프에서 노드는 리스트에서의 하나의 index에 해당이 되는 경우가 많은데,
이번 문제에서는 입력으로 주어진 전체 리스트가 하나의 노드 역할에 해당됩니다. 추가로 방문 여부를 확인하는 v(visited) 역시 집합으로
특정 문자열을 거친적이 있는 지 확인합니다. 배열이 집합의 인자로 들어갈 수 없기 때문에 문자열로 변환해야 합니다.([1,2] -> "12")

사실 bfs방식을 써서 그래프 문제라고 하였지만, heapq 방식을 써서 구현해도 똑같습니다.
리스트 전체가 그래프의 노드처럼 활용되는 새로운 방식의 문제였습니다.
"""
