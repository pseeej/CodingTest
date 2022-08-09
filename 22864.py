a, b, c, m = map(int, input().split())

tired = 0
time = 0
work = 0

while time < 24:
    # M 이하여야 되는 거니깐 등호도 필요함!
    if tired + a <= m:
        tired += a
        work += b
    else:
        tired -= c
        # 힘든 게 0 이하면 0으로 리셋되겠지~ 음수는 없으니깐~
        if tired < 0:
            tired = 0

    time += 1


print(work)
