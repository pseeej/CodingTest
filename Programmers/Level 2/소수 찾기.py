from itertools import permutations
def solution(numbers):
    answer = 0
    
    visited = set()
    for p in range(1, len(numbers)+1):
        perms = list(permutations(numbers, p))
        # print(perms)
        for perm in perms:
            num = ''.join(map(str, perm))
            num = int(num)
            if num not in visited:
                visited.add(num)
                
    
    primes = [True for _ in range(max(visited)+1)]
    primes[0] = False
    primes[1] = False
    
    for i in range(2, len(primes)):
        if primes[i]:
            num = i+i
            while num < len(primes):
                primes[num] = False
                num += i
                
    for num in visited:
        if primes[num]:
            answer += 1
                
        
    
    
    return answer
