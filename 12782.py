T = int(input())

for _ in range(T):
    N, M = map(str, input().split())
    
    result = 0
    cnt1 = 0
    cnt0 = 0
    for i in range(len(N)):
        if N[i] != M[i]:
            if N[i] == "1":
                cnt1 += 1
            else:
                cnt0 += 1
        
    result += min(cnt0, cnt1)
    result += (max(cnt0, cnt1)-min(cnt0, cnt1))

    print(result)
