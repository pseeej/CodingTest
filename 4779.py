import sys
input = sys.stdin.readline

def recursion(start, end, cantour):
    if end-start < 3:
        return

    mid = (end-start)//3
    for i in range(start+mid, end-mid):
        cantour[i] = " "
    
    recursion(start, start+mid, cantour)
    recursion(end-mid, end, cantour)


while True:
    try:
        N = int(input())

        cantour = ["-" for _ in range(3**N)]
        recursion(0, 3**N, cantour)

        print(''.join(cantour))
    except:
        break
