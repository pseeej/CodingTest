N = int(input())

nocall = {"3", "6", "9"}

for num in range(1, N+1):
    numli = list(str(num))

    cnt = 0
    for i in range(len(numli)):
        if numli[i] in nocall:
            cnt += 1

    if cnt == 0:
        print(num, end=" ")
    else:
        print("-"*cnt, end=" ")

