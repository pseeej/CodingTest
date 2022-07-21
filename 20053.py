T = int(input())

for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    print(min(li), max(li))
