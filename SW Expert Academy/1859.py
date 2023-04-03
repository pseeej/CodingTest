T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    profit = 0

    length = int(input())
    nums = list(map(int, input().split()))

    maxnum = 0
    for i in range(length-1, -1, -1):
        if nums[i] > maxnum:
            maxnum = nums[i]
        else:
            profit += maxnum - nums[i]

    print(f"#{test_case} {profit}")
