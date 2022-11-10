import sys
from collections import defaultdict
input = sys.stdin.readline

colors = defaultdict(list)
points = []

N = int(input())
for _ in range(N):
    x, color = map(int, input().split())
    colors[color].append(x)
    points.append((x, color))

for color in colors:
    colors[color].sort()

points = sorted(points, key= lambda item:item[0])

result = 0
for point in points:
    x, color = point
    idx = colors[color].index(x)
    if idx == 0:
        result += colors[color][1] - x
    elif idx == len(colors[color])-1:
        result += x - colors[color][idx-1]
    else:
        left = colors[color][idx-1]
        right = colors[color][idx+1]

        if x-left < right-x:
            result += x-left
        else:
            result += right-x

print(result)
