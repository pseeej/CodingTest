from collections import deque
from math import sqrt

def changenum(num, under):
    result = deque()
    
    while num > 0:
        result.appendleft(num%under)
        num //= under
        
    return ''.join(map(str, result))

def checkIfPrime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
        
    return True
    
    

def solution(n, k):
    answer = 0
    
    newnum = changenum(n, k)
    tmparr = newnum.split('0')
    newarr = []
    
    for num in tmparr:
        if len(num):
            newarr.append(int(num))
            
    for num in newarr:
        answer += checkIfPrime(num)
    
    
    return answer
