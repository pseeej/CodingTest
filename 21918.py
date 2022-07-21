N, M = map(int, input().split())
lights = list(map(int, input().split()))

for _ in range(M):
    order, x, y = map(int, input().split())
    if order == 1:
        lights[x-1] = y
    elif order == 2:
        for i in range(x-1, y):
             # 1과 0을 True/False로 보고 반대로 뒤집어주기
             # 일반 c에서는 !로 했겠지만 여기선 안 되길래 냅다 not 넣었는데 되더라
             # 대신 그냥 not으로만 두면 True, False로 뜨니깐 int로 해서 1, 0으로 나오게 함
            lights[i] = int(not(lights[i]))
    elif order == 3:
        for i in range(x-1, y):
            lights[i] = 0
    elif order == 4:
        for i in range(x-1, y):
            lights[i] = 1

print(*lights)
