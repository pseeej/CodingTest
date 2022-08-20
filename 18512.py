x, y, p1, p2 = map(int, input().split())

while True:
    if p2 < p1:
        p2 += y
    elif p2 == p1:
        print(p1)
        break
    else:
        p1 += x

    if p1 > 10000 or p2 > 10000:
        print("-1")
        break
