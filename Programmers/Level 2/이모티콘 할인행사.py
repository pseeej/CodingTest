from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    sales = [10, 20, 30, 40]
    products = list(product(sales, repeat=len(emoticons)))
    
    for prod in products:
        tmpanswer = [0, 0]
        for user in users:
            perc = user[0]
            yesan = user[1]
            
            totbuy = 0
            for i in range(len(emoticons)):
                # print((100-perc)/100)
                if perc <= prod[i]:
                    totbuy += emoticons[i]*((100-prod[i])/100)
                
            if totbuy >= yesan:
                tmpanswer[0] += 1
            else:
                tmpanswer[1] += totbuy
        
        
        if tmpanswer[0] > answer[0] or (tmpanswer[0] == answer[0] and tmpanswer[1] > answer[1]):
            # print(prod, tmpanswer)
            answer = tmpanswer
    
    
    
    return answer
