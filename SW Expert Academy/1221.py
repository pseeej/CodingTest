T = int(input())

str2num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
num2str = dict()
for elem in str2num:
    num2str[str2num[elem]] = elem

for i in range(1, T+1):
    test_case, length = input().split()
    test_case = int(test_case[1:])

    arr = list(map(str, input().split()))

    numarr = []
    for elem in arr:
        numarr.append(str2num[elem])

    numarr.sort()

    result = []
    for elem in numarr:
        result.append(num2str[elem])

    print(f"#{test_case}")
    print(' '.join(result))
