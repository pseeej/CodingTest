import sys
input = sys.stdin.readline

yaksus = [1 for _ in range(1000001)]
yaksums = [0 for _ in range(1000001)]

for i in range(2, 1000001):
    j = 1
    while i*j < 1000001:
        yaksus[i*j] += i
        j += 1


for i in range(1, 1000001):
    yaksums[i] = yaksums[i-1]+yaksus[i]

T = int(input())
for _ in range(T):
    num = int(input())
    print(yaksums[num])
