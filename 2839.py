N = int(input())

cnt = 0
while N > 0:
    if N % 5 == 0:
        cnt += 1
        N -= 5
    elif N % 3 == 0:
        cnt += 1
        N -= 3
    elif N >= 5:
        cnt += 1
        N -= 5
    else:
        break

if N != 0:
    print(-1)
else:
    print(cnt)
