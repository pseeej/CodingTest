import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
nums = [0]
for _ in range(N):
    nums.append(int(input()))

totgroups = set()

for i in range(1, N+1):
    upset = set()
    downset = set()

    currup = i
    upset.add(currup)
    downset.add(nums[currup])
    visited_up = set()

    while currup not in visited_up:
        visited_up.add(currup)

        currup = nums[currup]
        upset.add(currup)
        downset.add(nums[currup])

    if upset == downset:
        tmp = list(upset)
        tmp.sort()
        tmp = tuple(tmp)
        totgroups.add(tmp)
        
answer = []
for group in totgroups:
    for num in group:
        answer.append(num)

answer.sort()

print(len(answer))
for num in answer:
    print(num)
        

        
