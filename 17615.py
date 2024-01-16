import sys
input = sys.stdin.readline

N = int(input())
tmp = input().strip()
balls = []

reds = []
blues = []
for i in range(N):
    balls.append(tmp[i])
    if tmp[i] == 'R':
        reds.append(i)
    else:
        blues.append(i)

rleft = 0
rright = 0
for i in range(len(reds)):
    if i != reds[i]:
        rleft += 1
    if N-i-1 != reds[len(reds)-1-i]:
        # print(N-i-1, reds[len(reds)-i-1])
        rright += 1

bleft = 0
bright = 0
for i in range(len(blues)):
    if i != blues[i]:
        bleft += 1
    if N-i-1 != blues[len(blues)-i-1]:
        bright += 1

# print(rleft, rright, bleft, bright)
print(min(rleft, rright, bleft, bright))
        
