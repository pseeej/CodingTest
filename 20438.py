import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
sleeps = set(map(int, input().split()))
attends = set(map(int, input().split()))

attends = attends - sleeps

studs = [1 for i in range(N+3)] # 출첵 안 했으면 1, 했으면 0

for attend in attends:
    i = 1
    while attend*i < N+3:
        studs[attend*i] = 0
        i += 1

for sleep in sleeps:
    # i = 1
    # while sleep*i < N+3:
    #     studs[sleep*i] = 1
    #     print(sleep*i, end=" ")
    #     i += 1
    studs[sleep] = 1

# print()
# for i in range(N+3):
#     print(i, studs[i])

studs[:3] = [0 for i in range(3)]
for i in range(4, N+3):
    studs[i] = studs[i-1] + studs[i]

for _ in range(M):
    S, E = map(int, input().split())
    print(studs[E]-studs[S-1])
