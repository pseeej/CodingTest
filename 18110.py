import sys
input = sys.stdin.readline

def realRound(num):
    if num-int(num) >= 0.5:
        return int(num)+1
    
    return int(num)


N = int(input())
levels = []
for _ in range(N):
    levels.append(int(input()))

if len(levels) == 0:
    print(0)
    exit()

levels.sort()
cutnum = realRound(N*0.15)
levels = levels[cutnum:N-cutnum]

print(realRound(sum(levels)/len(levels)))
