from math import factorial
n, m = map(int, input().split())
if m > 0:
    known = list(map(int, input().split()))

# 주어진 숫자가 하나도 안 들어가는 거
# 하나만 들어가는 거,,, 이런 식으로
# 더했다가 뺐다가 더했다가 뺐다가 반복
count = 10
ans = 0
for i in range(m+1):
    ans += ((-1)**i)*(count**n)*(factorial(m)/(factorial(i)*factorial(m-i)))
    count -= 1

print(int(ans))
