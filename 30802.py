import sys
input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
shirts, pens = map(int, input().split())

reshirts = 0
for size in sizes:
    reshirts += size // shirts
    if size % shirts != 0:
        reshirts += 1

print(reshirts)
print(N//pens, N%pens)
