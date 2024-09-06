import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cakes = list(map(int, input().split()))

result = 0 # 10이면 안 잘라도 됨. 그냥 그거 그대로 하나의 롤케이크
intoten = []
elses = []

for cake in cakes:
    if cake == 10:  # 안 잘라도 됨. 그대로 하나의 롤케이크
        result += 1
    elif cake % 10 == 0:
        intoten.append(cake)
    else:
        elses.append(cake)

# 10으로 나눠지는 것들
intoten.sort()

for cake in intoten:
    while cake != 10:
        cake -= 10
        result += 1
        M -= 1

        if cake == 10:
            result += 1

        if M == 0:
            print(result)
            exit()


# 그냥 나머지 애들
for cake in elses:
    while cake > 10:
        cake -= 10
        result += 1
        M -= 1

        if cake == 10:
            result += 1

        if M == 0:
            print(result)
            exit()

print(result)
