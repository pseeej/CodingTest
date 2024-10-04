import sys
input = sys.stdin.readline

n = int(input())

if n < 0:
    oneback = 0
    twoback = 1
    for num in range(-1, n-1, -1):
        curr = (twoback - oneback)
        if curr > 0:
            curr = (curr%1000000000)
        twoback = oneback
        oneback = curr

        # print(dp)
    
    if curr > 0:
        print(1)
    elif curr == 0:
        print(0)
    else:
        print(-1)

    print(abs(curr)%1000000000)

elif n > 1:
    oneback = 1
    twoback = 0
    for num in range(2, n+1, 1):
        curr = (oneback + twoback)%1000000000
        twoback = oneback
        oneback = curr
    
    if curr > 0:
        print(1)
    elif curr == 0:
        print(0)
    else:
        print(-1)

    print(abs(curr)%1000000000)

else:
    if n == 0:
        print(0)
        print(0)
    elif n == 1:
        print(1)
        print(1)
