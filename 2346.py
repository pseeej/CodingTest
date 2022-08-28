import sys
input = sys.stdin.readline

N = int(input())

nums = [i for i in range(1, N+1)]
locs = list(map(int, input().split()))

# 현재 위치 저장하는 변수
curr = 0

while len(nums) > 1:
    # 현재 위치의 값 출력
    print(nums[curr], end=" ")
    # 현재 위치의 값은 빠지게 될 것이므로
    # 현재 위치 제외한 나머지 값들로 이뤄진 nums 할당
    # 따지고보면 nums.pop(curr)와 동일한 과정
    nums = nums[:curr] + nums[curr+1:]
    # print(nums, end=" ")

    # 다음 step을 loc에 저장
    loc = locs.pop(curr)
    # print(loc)
    
    # 만약 다음 step이 0 이상이면
    # 현위치 + step - 1 해줌. 양수값은 0부터 시작하기 때문에... 이거 다루려고...
    # %len(nums)는 nums의 범위 벗어나는 index 가지면 안되기 때문에!
    if loc > 0:
        curr = (curr+loc-1)%len(nums)
    # 음수값일 경우 -1 없이 그냥 바로 현위치 + step 해줌
    # 파이썬은 음수값도 나머지연산이 가능함
    else:
        curr = (curr+loc)%len(nums)

print(nums[0])
