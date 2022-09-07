import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
drinks = list(map(int, input().split()))

drinks.sort()
drinks = deque(drinks)

res = drinks.pop()

while drinks:
    res = res + drinks.popleft()/2

print(res)
