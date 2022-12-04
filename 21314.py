import sys
input = sys.stdin.readline

# M과 K는 나눠질 수 있지만
# M과 M끼리는 나눠질 수 없음.

# 가장 큰 경우는 K를 기준으로 잘랐을 때...의 덩이 (더 자르지 않음)
# 가장 작은 경우는 K를 하나씩 다 떼어서 왔을 때.

mknum = input().strip()

# 가장 큰 경우
largest = []
tmp = ''
for c in mknum:
    tmp += c
    if c == "K":
        largest.append(tmp)
        tmp = ""

if len(tmp):
    largest.append(tmp)

max_calc = ""
for elem in largest:
    if "K" in elem:
        max_calc += str(10 ** elem.count("M") * 5)
    else:
        max_calc += str("1") * elem.count("M")
        
print(max_calc)

# 가장 작은 경우
smallest = []
tmp = ""
for c in mknum:
    if c == "M":
        tmp += c
    else:
        if tmp:
            smallest.append(tmp)
        tmp = ""
        smallest.append(c)

if len(tmp):
    smallest.append(tmp)

#print(smallest)

min_calc = ""
for elem in smallest:
    if "K" in elem:
        min_calc += str(10 ** elem.count("M") * 5)
    else:
        min_calc += str(10 ** (elem.count("M") - 1))

print(min_calc)
