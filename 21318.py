import sys
input = sys.stdin.readline

N = int(input())
akbo = list(map(int, input().split()))
calc = [0 for _ in range(N+1)]

for i in range(N-1):
    if akbo[i+1] < akbo[i]:   # 다음 > 지금
        calc[i+1] = calc[i] + 1
    else:
        calc[i+1] = calc[i]

calc[-1] = calc[-2]

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(calc[y-1]-calc[x-1])
