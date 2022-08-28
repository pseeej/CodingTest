import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

nums = deque()
top = -1

for _ in range(N):
    order = input()

    if "push_front" in order:
        ord, num = order.split()
        nums.appendleft(num)
        top += 1
    elif "push_back" in order:
        ord, num = order.split()
        nums.append(num)
        top += 1
    elif "pop_front" in order:
        if top == -1:
            print("-1")
        else:
            print(nums.popleft())
            top -= 1
    elif "pop_back" in order:
        if top == -1:
            print("-1")
        else:
            print(nums.pop())
            top -= 1
    elif "size" in order:
        print(top+1)
    elif "empty" in order:
        if top == -1:
            print("1")
        else:
            print("0")
    elif "front" in order:
        if top == -1:
            print("-1")
        else:
            print(nums[0])
    elif "back" in order:
        if top == -1:
            print("-1")
        else:
            print(nums[top])
