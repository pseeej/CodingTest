from collections import deque

for _ in range(10):
    test_case = int(input())
    arr = deque(map(int, input().split()))

    minus = 1
    while arr[-1] > 0:
        num = arr.popleft()
        if num - minus <= 0:
            arr.append(0)
            break
        else:
            arr.append(num-minus)

        if minus < 5:
            minus += 1
        else:
            minus = 1

    print(f"#{test_case}", end=" ")
    for i in range(8):
        print(arr[i], end=" ")
    print()

