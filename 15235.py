from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

queue = deque()
for i in range(N):
    queue.append([arr[i], i])

result = [0 for _ in range(N)]
time = 0
while queue:
    time += 1
    curr = queue.popleft()
    newli = [curr[0]-1, curr[1]]

    if newli[0] == 0:
        result[curr[1]] = time
        continue
    else:
        queue.append(newli)


print(' '.join(map(str, result)))
