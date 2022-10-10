import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visits = list(map(int, input().split()))

result = 0
cnt = 1

visits.insert(0, 0)

for i in range(0, N+1):
    visits[i] += visits[i-1]

for i in range(N-X+1):
    now = visits[i+X] - visits[i]
    # print(i, now)
    if now > result:
        result = now
        cnt = 1
    elif now == result:
        cnt += 1

if result == 0:
    print("SAD")
else:
    print(result)
    print(cnt)
