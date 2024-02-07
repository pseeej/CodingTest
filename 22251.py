from collections import defaultdict
import sys
input = sys.stdin.readline
N, K, P, X = map(int, input().split())

nums = [[True, True, True, False, True, True, True],
        [False, False, True, False, False, True, False],
        [True, False, True, True, True, False, True],
        [True, False, True, True, False, True, True],
        [False, True, True, True, False, True, False],
        [True, True, False, True, False, True, True],
        [True, True, False, True, True, True, True],
        [True, False, True, False, False, True, False],
        [True, True, True, True, True, True, True],
        [True, True, True, True, False, True, True]]

changediff = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    a = nums[i]
    for j in range(10):
        if j == i:
            continue
        
        b = nums[j]
        cnt = 0
        for k in range(7):
            if a[k] != b[k]:
                cnt += 1

        changediff[i][j] = cnt
        
realnum = ['0' for _ in range(K)]
tmp = str(X)

for i in range(len(tmp)):
    realnum[K-len(tmp)+i] = str(int(realnum[K-len(tmp)+i]) + int(tmp[i]))

answer = 0
currint = 1

while currint <= N:
    currli = ['0' for _ in range(K-len(str(currint)))]
    currli.extend(list(str(currint)))

    cntdiff = 0
    for i in range(K):
        cntdiff += changediff[int(currli[i])][int(realnum[i])]

    # print(currint, cntdiff)
    if 1 <= cntdiff <= P:
        answer += 1
        # print(currint)

    currint += 1

print(answer)
