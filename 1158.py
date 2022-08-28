N, K = map(int, input().split())

nums = [i for i in range(1, N+1)]

cnt = 0
idx = 0
print("<", end="")
while len(nums) > 1:
    while cnt < K:
        # 범위 넘어가는 거 막기 위해
        if idx >= len(nums) :
            idx = 0
        # 제일 첫 시작은 idx 0부터니깐...
        # 이거 없으면 시작이 1부터 됨
        if cnt != 0:
            idx += 1
        cnt += 1

    # idx의 범위 벗어난 거 처리 위해
    if idx >= len(nums):
        idx = 0

    # 해당 값 list에서 제거
    print(nums.pop(idx), end=", ")
    cnt = 0

print(nums[0], end=">")
