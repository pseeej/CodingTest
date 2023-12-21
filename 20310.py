from collections import deque
import sys
input = sys.stdin.readline

N = input().strip()
cnt_0 = int(N.count('0')//2)
cnt_1 = int(N.count('1')//2)

# 0은 뒤에서부터 지우고
# 1은 앞에서부터 지우는 게 좋음

newli = []
for i in range(len(N)):
    newli.append(N[i])

del0 = 0
idx = len(N)-1
while del0 < cnt_0:
    if newli[idx] == '0':
        newli[idx] = -1
        del0 += 1
    idx -= 1

del1 = 0
idx = 0
while del1 < cnt_1:
    if newli[idx] == '1':
        newli[idx] = -1
        del1 += 1
    idx += 1

for i in range(len(N)):
    if newli[i] != -1:
        print(newli[i], end="")


