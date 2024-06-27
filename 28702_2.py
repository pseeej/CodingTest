import sys
input = sys.stdin.readline

for i in range(3):
    word = input().strip()
    if word.isdigit():
        result = int(word)+3-i
        if result%15 == 0:
            print("FizzBuzz")
        elif result%3==0 and result%5!=0:
            print("Fizz")
        elif result%3!=0 and result%5==0:
            print("Buzz")
        else:
            print(result)

        break
