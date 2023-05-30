def solution(players, callings):
    answer = []
    
    records = dict()
    for i in range(len(players)):
        records[players[i]] = i
        
    for call in callings:
        # 현재 불린 선수의 위치가 where. 이름은 call
        where = records[call]
        
        # 불린 선수 앞자리 선수 이름 tmp, 위치 where-1
        tmp = players[where-1]
        players[where-1] = call
        players[where] = tmp
        
        records[tmp] = where
        records[call] = where-1
        
    answer = players
        
    
    return answer
