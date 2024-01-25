import sys
input = sys.stdin.readline
N = int(input())
towers = list(map(int, input().split()))
signals = [-1 for _ in range(N)]

stack = [0]

for i in range(1, N):
    # print(stack)
    if towers[stack[-1]] > towers[i]:
        signals[i] = stack[-1]
    else:
        while len(stack) > 0  and towers[stack[-1]] <= towers[i]:
            stack.pop()
            
        if len(stack) > 0:
            signals[i] = stack[-1]
            
    stack.append(i)

for i in range(N):
    print(signals[i]+1, end=" ")
            
