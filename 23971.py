import sys
input = sys.stdin.readline

h, w, n, m = map(int, input().split())

sero = 0

if h%(n+1) == 0:
    sero += h//(n+1)
else:
    sero += h//(n+1)+1

garo = 0

if w%(m+1) == 0:
    garo += w//(m+1)
else:
    garo += w//(m+1)+1

print(sero*garo)
    
