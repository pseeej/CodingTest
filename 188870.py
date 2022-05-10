N = int(input())
inp = list(map(int, input().split()))

arr = dict()  # list의 index 연산은 복잡도가 너무 커서 대신에 dict 형태 사용
for el in inp:
    arr[el] = 0

tmp = sorted(list(set(arr)))

for i in range(len(tmp)):
    arr[tmp[i]] = i

# input 순서대로 가져와서 출력
for i in range(len(inp)):
    print(arr[inp[i]], end=" ")
