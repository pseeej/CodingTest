from collections import deque
from copy import deepcopy

def solution(bandage, health, attacks):
    answer = 0
    
    attacks = deque(attacks)
    endtime = attacks[-1][0]
    attack = attacks.popleft()
    atime, damage = attack[0], attack[1]
    
    aidstart = 0
    maxhealth = deepcopy(health)
    for t in range(endtime+1):
        # print(t, health)
        if atime != t:
            health += bandage[1]
            aidstart += 1
            
            if aidstart == bandage[0]:
                health += bandage[2]
                aidstart = 0
            
            if health > maxhealth:
                health = maxhealth
        else:
            health -= damage
            aidstart = 0
            if len(attacks) > 0:
                attack = attacks.popleft()
                atime, damage = attack[0], attack[1]
            
        if health <= 0:
            break
                
    if health <= 0:
        answer = -1
    else:
        answer = health
        
    return answer
