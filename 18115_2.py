from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
turns = list(map(int, input().split()))

idxs = [i for i in range(N)]
idxs = deque(idxs)
result = [0 for _ in range(N)]

num = N
for turn in turns:
    # 1일 때는 뒤에서부터 지우기. 그냥 pop
    if turn == 1:
        idx = idxs.pop()
        result[idx] = num
    elif turn == 2:
        tmp = idxs.pop()
        idx = idxs.pop()
        result[idx] = num
        idxs.append(tmp)
    else:
        idx = idxs.popleft()
        result[idx] = num

    # print(idxs)

    num -= 1

print(' '.join(map(str, result[::-1])))
        
    
