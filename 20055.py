from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
conveyor = deque(map(int, input().split()))
robots = [False for i in range(2*N)]
robots = deque(robots)
upseq = deque()

zerocnt = 0
turn = 0


while zerocnt < K:
    # print(conveyor, "\n", robots, "\n", upseq, end="\n")
    turn += 1
    
    # 한 칸 이동
    # 로봇과 함께...
    conveyor.appendleft(conveyor.pop())
    robots.appendleft(robots.pop())
    newlist = deque()

    for i in range(len(upseq)):
        upseq[i] = (upseq[i]+1)%(2*N)
        
        # 한 칸 돌았는데 그 위치가 N-1일 경우 빼버림
        if upseq[i] != N-1:
            newlist.append(upseq[i])
        else:
            robots[N-1] = False
            
    upseq = newlist

    # 가장 먼저 벨트에 올라간 로봇부터 움직이기
    newlist = deque()
    for i in range(len(upseq)):
        onConveyor = True
        
        nextidx = (upseq[i]+1)%(2*N)
        # 다음 위치가 N-1인데 이동 가능한 경우
        if nextidx == N-1 and conveyor[nextidx] >= 1 and robots[nextidx] == False:
            conveyor[N-1] -= 1
            if conveyor[N-1] == 0:
                zerocnt += 1
            onConveyor = False
            robots[N-1] = False
            robots[upseq[i]] = False
            continue
            
        if robots[nextidx] == False and conveyor[nextidx] >= 1:
            robots[nextidx] = True
            conveyor[nextidx] -= 1
            
            robots[upseq[i]] = False
            upseq[i] = nextidx
            
            # 내구도 0 되면
            if conveyor[nextidx] == 0:
                zerocnt += 1

        newlist.append(upseq[i])

    upseq = newlist

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
    if conveyor[0] >= 1 and robots[0] == False:
        upseq.append(0)
        robots[0] = True
        conveyor[0] -= 1

        if conveyor[0] == 0:
            zerocnt += 1
    
print(turn)
