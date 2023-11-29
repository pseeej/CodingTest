def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    stack = []
    
    for i in range(len(prices)):
        price = prices[i]
        
        for s, idx in stack:
            answer[idx] += 1
        
        while stack and stack[-1][0] > price:
            stack.pop()
        stack.append([price, i])
        
    
    return answer
