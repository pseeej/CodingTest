# 14891
from collections import deque
import sys
input = sys.stdin.readline

tobnis = []
for _ in range(4):
    tobnis.append(deque(input().strip()))

K = int(input())
for _ in range(K):
    tn, way = map(int, input().split())
    tn = tn-1

    # 메인 톱니 회전시키기
    '''
    if way == -1:
        tobnis[tn].append(tobnis[tn].popleft())
    else:
        tobnis[tn].appendleft(tobnis[tn].pop())
    '''

    turns = [0 for _ in range(4)]
    turns[tn] = way

    # 왼쪽 톱니 회전시키기
    curtn = tn
    leftn = tn-1
    while leftn >= 0:
        if tobnis[curtn][6] == tobnis[leftn][2]:
            break
        elif tobnis[curtn][6] != tobnis[leftn][2] and way == -1:
            turns[leftn] = 1
            # tobnis[leftn].appendleft(tobnis[leftn].pop())
            way = 1
        elif tobnis[curtn][6] != tobnis[leftn][2] and way == 1:
            turns[leftn] = -1
            # tobnis[leftn].append(tobnis[leftn].popleft())
            way = -1

        curtn, leftn = leftn, leftn-1

    # 오른쪽 톱니 회전시키기
    curtn = tn
    rightn = tn+1
    way = turns[tn]
    while rightn < 4:
        if tobnis[curtn][2] == tobnis[rightn][6]:
            break
        elif tobnis[curtn][2] != tobnis[rightn][6] and way == -1:
            turns[rightn] = 1
            # tobnis[rightn].appendleft(tobnis[rightn].pop())
            way = 1
        elif tobnis[curtn][2] != tobnis[rightn][6] and way == 1:
            turns[rightn] = -1
            # tobnis[rightn].append(tobnis[rightn].popleft())
            way = -1

        curtn, rightn = rightn, rightn+1

    for i in range(4):
        if turns[i] == 1:
            tobnis[i].appendleft(tobnis[i].pop())
        elif turns[i] == -1:
            tobnis[i].append(tobnis[i].popleft())
        # print(tobnis[i])
    # print()


answer = 0
for i in range(4):
    if tobnis[i][0] == '1':
        answer += 2**i

print(answer)
        
        
