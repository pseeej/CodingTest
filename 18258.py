import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()
top = -1
for _ in range(N):
    order = input()
    
    if "push" in order:
        ord, num = order.split()
        queue.append(num)
        top += 1
    elif "pop" in order:
        if top == -1:
            print("-1")
        else:
            print(queue.popleft())
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
            print(queue[0])
    elif "back" in order:
        if top == -1:
            print("-1")
        else:
            print(queue[top])
