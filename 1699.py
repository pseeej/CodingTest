from math import sqrt
import sys
input = sys.stdin.readline

target = int(input())
dps = [i for i in range(target+1)]

for curr in range(2, target+1):
    for num in range(1, curr+1):
        square = num*num
        if square > curr:
            break

        if dps[curr] > dps[curr-square]+1:
            dps[curr] = dps[curr-square]+1

# print(dps)
print(dps[target])
        
