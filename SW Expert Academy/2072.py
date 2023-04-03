import sys
input = sys.stdin.readline

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))

    result = 0
    for num in nums:
        if num%2 == 1:
            result += num

    print(f"#{test_case} {result}")
