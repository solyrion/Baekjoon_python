"""
https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/ -> 참고했습니다.

max/min heapq을 이용해서 풀려고 시도했으나 지속적인 시간초과가 발생해서 윗분의 블로그를 참고했습니다.
특정변수 ind를 heap에 같이 저장하고, v배열을 이용해서 삭제여부를 체크합니다. 제거하는 과정에서는 while문을 이용해서
0번째 heap의 인자가 삭제된적이 없을경우까지 돌린후 그 인자를 삭제해주며 v를 0으로 변경해줍니다.
"""
import sys, heapq
input = sys.stdin.readline


for _ in range(int(input())):
    v = [0] * 1000001
    min_h, max_h = [], []
    ans = []

    for i in range(int(input())):
        x, y = input().split()
        if x == 'I':
            heapq.heappush(min_h, (int(y), i))
            heapq.heappush(max_h, (-int(y), i))
            v[i] = 1
        else:
            if int(y) == 1:
                while max_h and not v[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    v[max_h[0][1]] = 0
                    heapq.heappop(max_h)
            else:
                while min_h and not v[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    v[min_h[0][1]] = 0
                    heapq.heappop(min_h)
    while min_h and not v[min_h[0][1]]:heapq.heappop(min_h)
    while max_h and not v[max_h[0][1]]:heapq.heappop(max_h)
    if max_h and min_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print("EMPTY")
