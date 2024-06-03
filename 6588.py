import sys
input = sys.stdin.readline

MAX = 1000000
primes = [True for _ in range(MAX+1)]

for i in range(2, MAX+1):
    j = 2
    while i * j <= MAX:
        primes[i*j] = False
        j += 1

realprimes = []
for i in range(2, MAX+1):
    if primes[i]:
        realprimes.append(i)

num = int(input())
while num != 0:
    idx = 0
    while not primes[num - realprimes[idx]] and idx <= MAX:
        idx += 1

    if idx <= MAX:
        print(f"{num} = {realprimes[idx]} + {num-realprimes[idx]}")
    else:
        print("Goldbach's conjecture is wrong")
        
    num = int(input())
