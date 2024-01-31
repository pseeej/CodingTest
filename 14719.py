import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

maxheight = max(blocks)
maxs = []

for i in range(W):
    if blocks[i] == maxheight:
        maxs.append(i)

result = 0

# 제일 큰 값 앞에
curr = blocks[0]
for i in range(1,maxs[0]):
    if blocks[i] < curr:
        # print(curr, blocks[i])
        result += curr-blocks[i]
    else:
        curr = blocks[i]

# 큰 값들 사이
for i in range(len(maxs)-1):
    for j in range(maxs[i]+1, maxs[i+1]):
        # print(maxheight, blocks[j])
        result += maxheight-blocks[j]

# 제일 큰 값 뒤에
curr = blocks[-1]
for i in range(W-2, maxs[-1], -1):
    if blocks[i] < curr:
        # print(curr, blocks[i])
        result += curr-blocks[i]
    else:
        curr = blocks[i]

print(result)
    
    
