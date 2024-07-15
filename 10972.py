import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
if len(nums) == 0:
    nums = []

if nums == [i for i in range(N, 0, -1)]:
    print(-1)
    exit()

idx = N-1
while idx >= 0:
    possnums = nums[idx:]
    possnums.sort()

    if nums[idx:] == possnums[::-1]:
        idx -= 1
    else:
        break

possnums = list({i for i in range(1, N+1)} - set(nums[:idx]))
possnums.sort()

if idx >=  0:
    firstnum = possnums[possnums.index(nums[idx])+1]
else:
    firstnum = ''
elsenums = list(set(possnums) - {firstnum})
elsenums.sort()

# print(nums, firstnum, elsenums)

result = []
for n in nums[:idx]:
    result.append(n)
if firstnum != '':
    result.append(firstnum)
for n in elsenums:
    result.append(n)

print(' '.join(map(str, result)))
