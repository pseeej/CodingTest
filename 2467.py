import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

left = 0
right = 0

checkIfYang = False
for i in range(N):
    if liquids[i] == abs(liquids[i]):
        right = i
        checkIfYang = True
        break

if not checkIfYang:
    right = N-1

result = float("inf")
nums = [0, 0]

if right+1 < N and abs(liquids[right+1]+liquids[right]) <= result:
    result = abs(liquids[right+1]+liquids[right])
    nums = [liquids[right], liquids[right+1]]
    # print(nums)

left = right-1
if left-1 >= 0 and abs(liquids[left-1]+liquids[left]) <= result:
    result= abs(liquids[left-1]+liquids[left])
    nums = [liquids[left-1], liquids[left]]
   #  print(nums)

while left >= 0 and right < N:
    tmp = liquids[left]+liquids[right]
    # print(liquids[left], liquids[right])

    if abs(tmp) < result:
        result = abs(tmp)
        nums = [liquids[left], liquids[right]]

    if tmp < 0:
        right += 1
    else:
        left -= 1

    

nums.sort()
for num in nums:
    print(num, end=" ")
