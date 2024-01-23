from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

checkIfDone = False

def DFS(now):
    # print(''.join(now))
    global checkIfDone, S
    if ''.join(now) == S:
        checkIfDone = True
        return
    
    if len(now) <= len(S):
        return

    if now[-1] == 'A':
        daum = deepcopy(now)
        daum.pop()
        DFS(daum)
        
    if now[0] == 'B':
        daum = deepcopy(now)
        daum.popleft()
        daum.reverse()
        DFS(daum)


newli = deque()
for c in T:
    newli.append(c)

# print(newli)
DFS(newli)

if checkIfDone:
    print(1)
else:
    print(0)
    
