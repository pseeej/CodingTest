from curses.ascii import isdigit
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dogam = dict()
dogam_list = list()
for i in range(1, N+1):
    name = input().strip()
    dogam[name] = i
    dogam_list.append(name)


for _ in range(M):
    sth = input().strip()
    if sth.isdigit():
        print(dogam_list[int(sth)-1])
    else:
        print(dogam[sth])
