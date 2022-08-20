vowels = "aeiou"

while True:
    pw = input()
    if pw == "end":
        break

    v_cnt = 0
    flag = 1    # 비밀번호 성립 여부 확인 플래그. 1이면 적합, 0이면 부적합

    for i in range(len(pw)):
        # 모음 개수 세어주기 위한 조건문
        if pw[i] in vowels:
            v_cnt += 1

        # 같은 글자가 연속 적으로 두 개 오는지 확인
        if i >= 1 and pw[i] == pw[i-1] and pw[i] not in ['e' ,'o']:
            flag = 0
            break
        
        # 모음이 세 개 혹은 자음이 세 개 연속으로 오는지 확인
        if i >= 2:
            # 다 모음인지
            if pw[i] in vowels and pw[i-1] in vowels and pw[i-2] in vowels:
                flag = 0
                break
            # 다 자음인지
            if pw[i] not in vowels and pw[i-1] not in vowels and pw[i-2] not in vowels:
                flag = 0
                break

    
    if flag == 0 or v_cnt == 0:
        print(f'<{pw}> is not acceptable.')
    else:
        print(f'<{pw}> is acceptable.')
    
