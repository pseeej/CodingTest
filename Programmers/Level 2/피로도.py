from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    perms = list(permutations(dungeons))
    for perm in perms:
        hp = k
        tmpcnt = 0
        for dg in perm:
            opened, closed = dg
            if hp >= opened:
                tmpcnt += 1
                hp -= closed
        
        answer = max(answer, tmpcnt)
    
    return answer
