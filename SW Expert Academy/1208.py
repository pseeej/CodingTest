from collections import deque

for test_case in range(1, 11):
    dump = int(input())

    arr = deque(map(int, input().split()))
    arr = deque(sorted(arr))

    for _ in range(dump):
        shortest = arr.popleft()+1
        longest = arr.pop()-1

        for i in range(len(arr)):
            if shortest <= arr[i]:
                break

        arr.insert(i, shortest)

        for i in range(len(arr)-1, 0, -1):
            if longest >= arr[i]:
                break

        arr.insert(i, longest)

    print(f"#{test_case} {arr[-1]-arr[0]}")
