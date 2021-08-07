def solution(lottos, win_nums):
    answer = []
    
    lowest = len(set(lottos) & set(win_nums))
    highest = lowest + lottos.count(0)
    
    answer = [highest, lowest]
    
    for i in range(len(answer)):
        rank = answer[i]
        if rank == 6:
            answer[i] = 1
        elif rank == 5:
            answer[i] = 2
        elif rank == 4:
            answer[i] = 3
        elif rank == 3:
            answer[i] = 4
        elif rank == 2:
            answer[i] = 5
        else:
            answer[i] = 6
    
    return answer
