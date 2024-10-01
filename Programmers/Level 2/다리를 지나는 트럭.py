from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    bridge = [0 for _ in range(bridge_length-1)]
    bridge = deque(bridge)
    truck_weights = deque(truck_weights)
    bridge.append(truck_weights.popleft())

    sums = bridge[-1]
    
    while truck_weights:
        sums -= bridge.popleft()
            
        if sums+truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
            sums += bridge[-1]
        else:
            bridge.append(0)
        
        answer += 1
        
    return answer + bridge_length
