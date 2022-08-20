sent = input()

word = ""
result = ""
brckt_flag = 0
for i in range(len(sent)):
    # 공백이 나옴으로써 단어 끝난 거 확인. 근데 특수문자 안이 아니어야함
    # 아니면 지금까지 모아둔 글자들 뒤집어서 result에 삽입
    if sent[i] == " " and brckt_flag == 0:
        result += word[::-1] + " "
        word = ""
    # 특수문자 시작 시 brckt_flag로 표기.
    # 지금까지 모아둔 글자들 뒤집어서 result에 삽입
    elif sent[i] == "<":
        brckt_flag = 1
        result += word[::-1] + "<"
        word = ""
    # 특수문자 종료 시 brckt_flag 원래대로 0으로 바꿈
    # 특수문자 안에 있는 글자들은 그냥 원래 배열 그대로 result에 삽입
    elif sent[i] == ">":
        result += word + ">"
        word = ""
        brckt_flag = 0
    # 일반 문자/숫자면 단어에 글자 저장.
    else:
        word += sent[i]
        # 제일 마지막 글자 처리
        if i == len(sent)-1:
            result += word[::-1]

  
print(result)    
