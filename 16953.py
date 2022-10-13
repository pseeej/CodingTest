A, B = map(int, input().split())

cnt = 0
while B > A:
    # print(B)
    # 제일 마지막 자리가 1이면
    # 1 제거해준 값을 그 다음의 B값으로.
    if str(B)[-1] == "1":
        cnt += 1
        B = int(str(B)[:-1])
    
    else:
        if B%2:
            break
        B //= 2
        cnt += 1

if B==A:
    print(cnt+1)
else:
    print(-1)
