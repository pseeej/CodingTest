import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    tmp = list(map(int, input().split()))
    T, arr = tmp[0], tmp[1:]

    cnt = 0

    for i in range(0, 19):
        for j in range(i+1, 20):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                cnt += 1


    print(T, cnt)
