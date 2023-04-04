from string import ascii_uppercase, ascii_lowercase

T = int(input())

# 주어진 encoding 표 구현
base64 = dict()
idx = 0
for upp in ascii_uppercase:
    base64[upp] = idx
    idx += 1

for low in ascii_lowercase:
    base64[low] = idx
    idx += 1

for i in range(10):
    base64[str(i)] = idx
    idx += 1

base64["+"] = 62
base64["/"] = 63

for test_case in range(1, T + 1):
    dec_bin = ""
    result = ""
    sent = input()

    # 해당 문자에 해당되는 값 가져오기
    for s in sent:
        decoded = base64[s]

        # 2진수 변환
        decoded = format(decoded, 'b')

        # 자릿수 맞춰주기
        decoded = "0" * (6-len(decoded)) + decoded

        dec_bin += decoded

    # 8개씩 잘라서
    for idx in range(0, len(dec_bin), 8):
        tmpbin = dec_bin[idx:idx+8]

        # 2진수를 10진수로 변환해주기
        decimal = int(f'0b{tmpbin}', 2)

        # 해당 10진수값을 ascii로 변환
        result += chr(decimal)

    print(f"#{test_case} {result}")
