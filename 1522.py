from collections import deque
import sys
input = sys.stdin.readline

sent = input().strip()
chars = []
for s in sent:
    chars.append(s)
N = len(chars)

# a를 바꾼다고 할 때...
# 그럼 b가 연속이어야지
length = chars.count('b')
nowcnt = chars[:length].count('a')
result = nowcnt
for i in range(1, N):
    if chars[i-1] == 'a':
        nowcnt -= 1
    if chars[(i+length-1)%N] == 'a':
        nowcnt += 1
    
    result = min(nowcnt, result)

# b를 바꾼다고 할 때
# 그럼 a가 연속이어야지
length = chars.count('a')
nowcnt = chars[:length].count('b')
result = min(result, nowcnt)
for i in range(1, N):
    if chars[i-1] == 'b':
        nowcnt -= 1
    if chars[(i+length-1)%N] == 'b':
        nowcnt += 1

    result = min(nowcnt, result)

print(result)
