import sys
input = sys.stdin.readline

N = int(input())

li = []
top = -1

for _ in range(N):
    order = input()

    if "push" in order:
        num = order.split()[1]
        li.append(int(num))
        top += 1
    elif "pop" in order:
        if top == -1:
            print("-1")
        else:
            print(li.pop())
            top -= 1
    elif "size" in order:
        print(top+1)
    elif "empty" in order:
        if top == -1:
            print("1")
        else:
            print("0")
    elif "top" in order:
        if top == -1:
            print("-1")
        else:
            print(li[top])



'-----------------------------------------------------'
N = int(input())

li = []

for _ in range(N):
    order = input()

    if "push" in order:
        num = order.split()[1]
        li.append(int(num))
    elif "top" in order:
        if len(li) == 0:
            print("-1")
        else:
            print(li[-1])
    elif "size" in order:
        print(len(li))
    elif "pop" in order:
        if len(li) == 0:
            print("-1")
        else:
            print(li.pop())
    elif "empty" in order:
        if len(li) == 0:
            print("1")
        else:
            print("0")
