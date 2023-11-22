from collections import deque

def solution(n, t, m, p):
    answer = ''
    
    after10 = ['A', 'B', 'C', 'D', 'E', 'F']
    
    num2n = ["0"]
    for num in range(t*m):
        dec2n = deque()
        while num != 0:
            if num%n >= 10:
                dec2n.appendleft(after10[num%n%10])
            else:
                dec2n.appendleft(str(num%n))
            num //= n
        # print(dec2n)
        num2n.extend(dec2n)
        
    idx = 0
    # print(''.join(num2n))
    while len(answer) < t:
        if idx%m == p-1:
            answer += num2n[idx]
        idx += 1
    
    return answer
