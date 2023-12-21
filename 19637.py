import sys
input = sys.stdin.readline

N, M = map(int, input().split())
levels = dict()

levels = []
onlyfights = []
for _ in range(N):
    name, fight = map(str, input().split())
    fight = int(fight)
    levels.append(name)
    onlyfights.append(fight)

def binsearch(val, left, right, onlyfights):
    if right - left <= 1 or onlyfights[right] == val:
        print(levels[right])
        return
    
    mid = left + (right-left)//2

    if onlyfights[left] < val <= onlyfights[mid]:
        # print("LEFT", mid, end=" / ")
        binsearch(val, left, mid, onlyfights)
    else:
        # print("right", mid,  end=" / ")
        binsearch(val, mid, right, onlyfights)

for _ in range(M):
    num = int(input())
    if num <= onlyfights[0]:
        print(levels[0])
        continue
    binsearch(num, 0, N-1, onlyfights)

