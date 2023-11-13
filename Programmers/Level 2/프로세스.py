from collections import deque
def solution(priorities, location):
    answer = 0
    
    priorities = deque(priorities)
    maxpr = max(priorities)
    
    while True:
        if location == 0 and priorities[0] == maxpr:
            answer += 1
            break
        elif location == 0:
            location = len(priorities)
            priorities.append(priorities.popleft())
        elif priorities[0] == maxpr:
            answer += 1
            priorities.popleft()
            maxpr = max(priorities)
        else:
            priorities.append(priorities.popleft())
        
        location -= 1
        
        
    
    return answer
