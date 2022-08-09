from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

c = list(combinations(nums, 3))

res = 0
for comb in c:
    comb_sum = sum(comb)
    
    # 작거나 같으면서, M에 최대한 가까워야 함(뺄셈 계산으로 dist 구함)
    if comb_sum <= M and M-comb_sum <= M-res:
        res = comb_sum

print(res)
        
