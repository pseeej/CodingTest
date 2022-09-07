import sys
input = sys.stdin.readline

N = int(input())
geun = list(map(int, input().split()))

geun.sort()

high = 0
if N%2 == 0:
    for i in range(N//2):
        calc = geun[i] + geun[N-1-i]
        if high < calc:
            high = calc
else:
    high = geun[-1]
    for i in range(N//2):
        calc = geun[i] + geun[N-2-i]
        if high < calc:
            high = calc

print(high)
