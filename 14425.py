N, M = map(int, input().split())

arr = set()
for i in range(N):
    arr.add(input())

cnt = 0
for i in range(M):
    word = input()
    if word in arr:
        cnt += 1

print(cnt)
