import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = []
for _ in range(N):
    belt.append(int(input()))

front = 0
back = k-1
chobabs = deque()

for i in range(k):
    chobabs.append(belt[i])
    
shobabs = set(chobabs)
result = 0

while front < N:
    shobabs = set(chobabs)
    if c not in shobabs:
        shobabs.add(c)
    result = max(result, len(shobabs))
    
    chobabs.popleft()
    front += 1
    back = (back+1)%N
    chobabs.append(belt[back])
    
    # print(chobabs)
    
if c not in shobabs:
    result += 1
        
print(result)
