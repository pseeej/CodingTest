from itertools import permutations
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
combs = list(permutations(nums, M))

combs.sort()

for comb in combs:
    for c in comb:
        print(c, end=" ")
    print()


'''
내장함수 안 쓴 거
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = []

def recurr(curnums):
    if len(curnums) == M:
        result.append(curnums)
        return
    
    setnums = set(nums)
    setcurrs = set(curnums)

    newnums = setnums - setcurrs

    for newnum in newnums:
        recurr(curnums+[newnum])


for n in nums:
    recurr([n])

result.sort()
for res in result:
    for r in res:
        print(r, end=" ")
    print()
'''
