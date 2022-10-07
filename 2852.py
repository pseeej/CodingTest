import sys
input = sys.stdin.readline

N = int(input())
score = [[0,0], [0,0]]
wincnt = {0:0, 1:0}
winningteam = 0

# time1과 time2 사이 몇 분인지 계산
def timedist(time1, time2):
    res = [0, 0]
    for i in range(2):
        res[i] = time2[i]-time1[i]

    # 초가 만약 마이너스라면
    if res[1] < 0:
        res[0] -= 1
        res[1] += 60

    # 초가 만약 60초를 넘었다면
    if res[1] >= 60:
        res[0] += 1
        res[1] -= 60

    return res

# score에 time 더해주기
def addtime(score, time):
    for i in range(2):
        score[i] += time[i]

    # 초가 만약 60초를 넘었다면
    if score[1] >= 60:
        score[0] += 1
        score[1] -= 60
        
    return score

winningteam, time = map(str, input().split())
prevtime = list(map(int, time.split(":")))
winningteam = int(winningteam)
wincnt[winningteam-1] += 1

for _ in range(N-1):
    team, time = map(str, input().split())
    curtime = list(map(int, time.split(":")))
    dist = timedist(prevtime, curtime)

    # 지금까지 이기고 있던 팀에다가 시간 더해주기
    # 비기고 있으면 상관 없음ㅋ
    if wincnt[winningteam-1] != wincnt[(not (winningteam-1))]:
        score[winningteam-1] = addtime(score[winningteam-1], dist)
    prevtime = curtime

    wincnt[int(team)-1] += 1
    # 이번에 점수를 얻음으로써 새로 이기고 된 팀 구하기
    if wincnt[winningteam-1] < wincnt[not (winningteam-1)]:
        winningteam = (not winningteam-1) + 1

# 제일 마지막까지 이기고 있던 팀은 (비기고 있으면 안 해줘도 됨)
# prevtime부터 48분까지 우승하고 있었던 거니깐...! 그 계산 해주기
if wincnt[winningteam-1] != wincnt[(not (winningteam-1))]:
    score[winningteam-1] += addtime(score[winningteam-1], timedist(prevtime, [48,0]))

def change2str(eachtime):
    if eachtime < 10:
        return "0"+str(eachtime)
    else:
        return eachtime

print(f"{change2str(score[0][0])}:{change2str(score[0][1])}")
print(f"{change2str(score[1][0])}:{change2str(score[1][1])}")
