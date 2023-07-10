from collections import deque
import math

N, D = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

infected = [False] * N
infected[0] = True

queue = deque([0])

while queue:
    current = queue.popleft()
    for i in range(N):
        if infected[i] or math.sqrt((XY[current][0] - XY[i][0])**2 + (XY[current][1] - XY[i][1])**2) > D:
            continue
        infected[current] = True
        queue.append(i)

for i in infected:
    print('Yes' if i else 'No')