N = int(input())

keep = N
cnt = 0

while True:
    sum_ = N//10 + N%10
    temp = N%10 * 10 + (sum_%10)
    if(temp==keep):
        cnt += 1
        break
    else:
        N = temp
        cnt += 1

print(cnt)