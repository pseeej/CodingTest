import sys
from collections import deque
input = sys.stdin.readline

nums = input().strip()
dnums = deque()
for i in range(len(nums)):
    dnums.append(nums[i])

checkIfDone = False

nownum = 1
while dnums:
    curr = dnums[0]
    strnum = str(nownum)
    checkIfDone = False
    
    for i in range(len(strnum)):
        if strnum[i] == curr:
            dnums.popleft()
            if len(dnums) == 0:
                checkIfDone = True
                break
            curr = dnums[0]

    if checkIfDone:
        break

    nownum += 1     

if checkIfDone:
    print(nownum)
else:
    print(nownum-1)
        
