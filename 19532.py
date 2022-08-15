a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        res1 = a*i + b*j
        res2 = d*i + e*j

        if res1 == c and res2 == f:
            print(i, j)
            exit()
