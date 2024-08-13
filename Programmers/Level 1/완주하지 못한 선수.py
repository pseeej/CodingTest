from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    partscnt = defaultdict(int)
    compscnt = defaultdict(int)
    
    for part in participant:
        partscnt[part] += 1
    
    for comp in completion:
        compscnt[comp] += 1
        
    for part in partscnt.keys():
        if partscnt[part] != compscnt[part]:
            return part
    
    return answer
