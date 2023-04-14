import sys
input = sys.stdin.readline

N = int(input())
arr = []
numset = set()

for _ in range(N):
    arr.append(int(input().strip()))
    numset.add(arr[-1])

numset = list(numset)

maxcnt = 0
cnt = 0

for num in numset:
    newarr = []
    for i in range(N):
        if arr[i] != num:
            newarr.append(arr[i])

    if len(newarr) == 0:
        maxcnt = max(0, maxcnt)
        continue
    
    cnt = 1
    befnum = newarr[0]
    for i in range(1,len(newarr)):
        if befnum == newarr[i]:
            cnt += 1
        else:
            befnum = newarr[i]
            maxcnt = max(maxcnt, cnt)
            cnt = 1

maxcnt = max(maxcnt, cnt)
print(maxcnt)
