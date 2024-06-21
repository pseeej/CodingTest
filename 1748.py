import sys
input = sys.stdin.readline

N = int(input())

result = 0
already = 1
cnt = 1
while N >= 10**cnt:
    result += cnt*(10**cnt-already)
    already += 10**cnt-already
    cnt += 1

    # print(result, already, cnt)

result += (N-already+1)*cnt

print(result)
