import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

calcd = [0 for i in range(N+1)]

calcd[0] = 0
for i in range(1, N+1):
    calcd[i] = calcd[i-1] + nums[i-1]


for _ in range(M):
    i, j = map(int, input().split())
    print(calcd[j]-calcd[i-1])
