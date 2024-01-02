import sys
input = sys.stdin.readline

storage = [0 for _ in range(1001)]

N = int(input())
length = 0
for _ in range(N):
    L, H = map(int, input().split())
    storage[L] = H
    length = max(L, length)

length = length+1
storage = storage[:length]
maxheight = max(storage)
# print(storage, maxheight)

start = 1001
end = 0
for i in range(length):
    if storage[i] == maxheight:
        start = min(start, i)
        end = max(end, i)

result = 0

# 왼쪽 구하기
currh = storage[0]
for i in range(start):
    if storage[i] > currh:
        currh = storage[i]
        result += storage[i]
    else:
        result += currh

# 가운데 구하기
for i in range(start, end+1):
    result += maxheight

# 오른쪽 구하기
currh = storage[-1]
for i in range(length-1, end, -1):
    if storage[i] > currh:
        currh = storage[i]
        result += storage[i]
    else:
        result += currh

print(result)
