def getRank(rank):
    rank_list = [6, 5, 4, 3, 2, 1]
    
    if rank != 0:
        return rank_list.index(rank)+1
    
    return 6
    

def solution(lottos, win_nums):
    answer = []
    
    lowest = len(set(lottos) & set(win_nums))
    highest = lowest + lottos.count(0)
    
    answer = [getRank(highest), getRank(lowest)]
    
    return answer
