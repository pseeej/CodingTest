import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
answer = [ -1 for _ in range(N)]

for idx in range(N):
    num = nums[idx]
    cnt = 0
    for i in range(N):
        if answer[i] == -1 and cnt == num:
            answer[i] = idx+1
            break
        
        if answer[i] == -1:
            cnt += 1

for an in answer:
    print(an, end=" ")
