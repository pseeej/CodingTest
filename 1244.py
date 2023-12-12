import sys
input = sys.stdin.readline

N = int(input())
switches = list(map(int, input().split()))
stu = int(input())
for _ in range(stu):
    gender, num = map(int, input().split())

    if gender == 1:
        for idx in range(num-1, N, num):
            switches[idx] = not switches[idx]

    else:
        idx = num-1
        switches[idx] = not switches[idx]
        
        size = 1
        while idx+size < N and idx-size >= 0 and switches[idx+size] == switches[idx-size]:
                switches[idx+size] = not switches[idx+size]
                switches[idx-size] = not switches[idx-size]
                size += 1

for i in range(N):
    if i > 0 and i % 20 == 0:
        print()
    if switches[i]:
        print(1, end=" ")
    else:
        print(0, end=" ")
