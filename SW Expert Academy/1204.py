from collections import defaultdict
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    trial = int(input())
    counts = defaultdict(int)
    nums = list(map(int, input().split()))
    for num in nums:
        counts[num] += 1
        
    sorteddict = sorted(counts.items(), key=lambda item:(-item[1], -item[0]))
    # print(sorteddict)
    print(f"#{trial} {sorteddict[0][0]}")
