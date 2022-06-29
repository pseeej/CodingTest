def solution(s):
    answer = ""
    
    # 숫자에 따른 영단어 저장
    alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    # 알파벳 한 글자씩을 저장할 임시 문자열 변수
    tmp = ""
    # 한 글자씩 돌면서 진행
    for alpha in s :
        # 숫자일 경우 바로 answer에 집어넣음
        if alpha.isdigit():
            answer += alpha
        # 숫자가 아닐 경우
        else:
            # tmp에 추가
            tmp += alpha
            # tmp가 완성된 한 단어일 경우
            if tmp in alphabet:
                # 정답 변수에 숫자값을 추가하고
                answer += str(alphabet.index(tmp))
                # 임시변수 초기화
                tmp = ""
    
    return int(answer)
