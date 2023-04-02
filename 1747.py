import sys
input = sys.stdin.readline

N = int(input())

while True:
    isprime = 1
    for i in range(2, int(N**(1/2)+1)):
        if N%i == 0:
            isprime = 0
            break

    if isprime==0 or N == 1:
        N += 1
        continue

    if str(N) == str(N)[::-1]:
        break

    N += 1

print(N)
