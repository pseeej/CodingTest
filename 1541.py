import sys
input = sys.stdin.readline

sent = input()

ops = []    # 연산자만 넣을 리스트
nums = []   # 숫자만 넣을 리스트

# 숫자와 연산자 분리해서 각각 ops와 nums에 넣어주는 과정
num = ""
for i in range(len(sent)):
    if sent[i].isdigit():
        num += sent[i]
    else:
        nums.append(int(num))
        num = ""

        if i != len(sent)-1:
            ops.append(sent[i])


res = 0
sums = []
while ops:
    # 연산자 하나씩 pop 해오면서
    op = ops.pop()
    # -가 나오면 이전에 + 묶어줬던 값들의 합 result에서 빼주기
    if op == "-":
        sums.append(nums.pop())
        res -= sum(sums)
        sums = []
    # +가 나오면 한꺼번에 묶어서 뺄셈 해주기 위해... sums라는 리스트에 추가
    elif op == "+":
        sums.append(nums.pop())

# 제일 마지막 값 처리
res += nums.pop()
# sums에 값 남아있을 경우 처리
if sums:
    res += sum(sums)
print(res)
