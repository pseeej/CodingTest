# Simulation Version

import sys
input = sys.stdin.readline

N = int(input())
turns = list(map(int, input().split()))

nums = [0 for _ in range(1, N+1)]
idxs = {1:N-1, 2:(N-2)%N, 3:0}

def findNewIdx(nums, idx, idxs, turn):
    if turn == 3:
        for i in range(idx, len(nums)):
            if nums[i] == 0:
                idxs[3] = i
                return idxs

    if turn == 1:
        idxs[1] = idxs[2]
    
    for i in range(idxs[2]-1, -1, -1):
        if nums[i] == 0:
            idxs[2] = i
            break

    return idxs
            

for i in range(N):
    currnum = N-i

    nums[idxs[turns[i]]] = currnum
    idxs = findNewIdx(nums, idxs[turns[i]], idxs, turns[i])

    # print(idxs, nums)


print(' '.join(map(str, nums[::-1])))
