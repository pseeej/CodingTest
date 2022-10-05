import sys
input = sys.stdin.readline

N, length = map(int, input().split())
pipes = list(map(int, input().split()))
pipes.sort()

i = 0
start = pipes[i] - 0.5
end = start + length
count = 0
while i < N:
    if start <= pipes[i] <= end:
        pass
    else:
        count += 1
        start = pipes[i] - 0.5
        end = start + length
    
    i += 1

print(count+1)
