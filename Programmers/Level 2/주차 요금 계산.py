from collections import defaultdict

def timediff(start, end):
    result = 0
    
    starthr, startmin = map(int, start.split(":"))
    endhr, endmin = map(int, end.split(":"))
    
    if endmin < startmin:
        result += endmin + 60 - startmin
        result += (endhr-1-starthr) * 60
    else:
        result += (endhr-starthr) * 60 + (endmin-startmin)
        
    return result

def solution(fees, records):
    answer = []
    tottimes = defaultdict(int)
    plotcars = dict()
    
    stdtime, stdfee, addtime, addfee = fees
    
    for record in records:
        time, carnum, intype = record.split()
        if intype == "IN":
            plotcars[carnum] = time
        else:
            tottimes[carnum] += timediff(plotcars[carnum], time)
            # print(carnum, time, plotcars[carnum], timediff(plotcars[carnum], time))
            plotcars.pop(carnum)
            
    for car in plotcars:
        tottimes[car] += timediff(plotcars[car], "23:59")
        
    totlist = sorted(tottimes.items(), key=lambda k:k[0])
    # print(totlist)
    for car, calctime in totlist:
        tot = stdfee
        calctime = max(calctime-stdtime, 0)
        # print(calctime, addtime)
        
        if calctime // addtime >= 0 and calctime % addtime > 0:
            tot += addfee * (calctime//addtime+1)
        else:
            tot += addfee * (calctime//addtime)
        answer.append(tot)
    
    return answer
