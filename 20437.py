from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sent = input().strip()
    K = int(input())


    charidxs = defaultdict(list)
    for i in range(len(sent)):
        charidxs[sent[i]].append(i)

    minlength = float("inf")

    # 가장 긴 연속 문자열의 길이
    maxlength = 0
    for c in charidxs:
        if len(charidxs[c]) >= K:
            # print(charidxs[c])
            for i in range(len(charidxs[c])-K+1):
                minlength = min(minlength, charidxs[c][i+K-1]-charidxs[c][i]+1)
                maxlength = max(maxlength, charidxs[c][i+K-1]-charidxs[c][i]+1)
 
    
    if minlength != float("inf") and maxlength != 0:
        print(minlength, maxlength)
    else:
        print(-1)
