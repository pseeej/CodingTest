X,Y,P1,P2 = map(int, input().split())
while True:
    if(P1==P2):
        print(P1)
        exit()
    elif(P1>10000):
        print(-1)
        exit()
    if(P1<P2):
        P1+=X
    else:
        P2+=Y
