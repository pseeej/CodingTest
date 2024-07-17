import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

if nums == [i for i in range(1, N+1)]:
    print(-1)
    exit()

idx = N-1
possnums = []
while idx >= 0:
    possnums = list({i for i in range(1, N+1)} - set(nums[:idx]))
    possnums.sort()
    # print(possnums)

    if nums[idx:] != possnums:
        break

    idx -= 1

result = nums[:idx]
if idx > 0:
    midnum = possnums[possnums.index(nums[idx])-1]
    result.append(midnum)
    possnums = set(possnums)
    possnums.remove(midnum)
    possnums = list(possnums)
    possnums.sort(reverse=True)
result.extend(possnums)

print(' '.join(map(str, result)))
        
    
