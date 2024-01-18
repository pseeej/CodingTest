import sys
input = sys.stdin.readline

N, K = map(int, input().split())

road = [0 for i in range(100001)]

# N 앞의 자리들
for i in range(N-1, -1, -1):
    road[i] = N-i

road[N] = 0
    
# N 뒤의 자리들
for i in range(N+1, 100001, 1):
    road[i] = i-N

# 순간이동
for i in range(100001):
    if i-1 >= 0 and road[i-1]+1 < road[i]:
        road[i] = road[i-1]+1
    if i+1 < 100001 and road[i+1]+1 < road[i]:
        road[i] = road[i+1]+1
    if i*2 < 100001 and road[i*2] > road[i]:
        road[i*2] = road[i]

print(road[K])




