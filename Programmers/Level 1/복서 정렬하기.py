def solution(weights, head2head):
    answer = []
    gamewin = [] # 승률 저장
    
    for i in range(len(head2head)):
        tempList = []
        one = head2head[i]
        for j in range(len(weights)):
            if one[j] == "L":
                tempList.append(0)
            elif one[j] == "N":
                tempList.append(-1)
            elif one[j] == "W" and weights[i] < weights[j]:   # 나보다 무거운 애 이김
                tempList.append(2)
            else:
                tempList.append(1)
        gamewin.append(tempList)
    weightRank = sorted(weights)
        
    # (승률, 무거운 애 이긴 횟수, 자기 몸무게 순위, 작은 번호)
    newList = []
    for i in range(len(gamewin)):
        game = gamewin[i]
        tempList = []
        if sum(game) == -1*len(gamewin):
            tempList.append(0)
        else:
            tempList.append((game.count(2)+game.count(1))/(len(gamewin)-game.count(-1)))
        tempList.append(game.count(2))
        tempList.append(weightRank.index(weights[i]))
        tempList.append(i)
        newList.append(tempList)

    newList = sorted(newList, key=lambda x:(-x[0], -x[1], -x[2], x[3]))
    for i in range(len(newList)):
        answer.append(newList[i][3]+1)
    
    return answer
