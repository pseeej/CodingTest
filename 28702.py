import sys
input = sys.stdin.readline

words = []
for _ in range(3):
    words.append(input().strip())

def changeByRules(num):
    if num%3 == 0 and num%5 == 0:
        return "FizzBuzz"
    elif num%3 == 0 and num%5 != 0:
        return "Fizz"
    elif num%3 != 0 and num%5 == 0:
        return "Buzz"
    else:
        return str(num)


if words[0] == "FizzBuzz":
    uppernum = 15
elif words[0] == "Fizz":
    uppernum = 3
elif words[0] == "Buzz":
    uppernum = 5
else:
    print(changeByRules(int(words[0])+3))
    exit()

current = uppernum
while True:
    if words[1] == changeByRules(current+1) and words[2] == changeByRules(current+2):
        print(changeByRules(current+3))
        break
    else:
        current += uppernum
