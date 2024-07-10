import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

k = int(input())
brackets = list(map(str,input().split()))

results = []
def checkSequence(curseq, idx):
    if idx >= len(brackets):
        newnum = ''.join(map(str, curseq))
        results.append(newnum)
        return

    allnums = {i for i in range(10)}
    leftnums = allnums - set(curseq)

    for num in leftnums:
        if brackets[idx] == ">" and curseq[-1] > num:
            curseq.append(num)
            checkSequence(curseq, idx+1)
            curseq.pop()
        elif brackets[idx] == "<" and curseq[-1] < num:
            curseq.append(num)
            checkSequence(curseq, idx+1)
            curseq.pop()
        else:
            continue

for i in range(10):
    checkSequence([i], 0)

results.sort()
print(results[-1])
print(results[0])
