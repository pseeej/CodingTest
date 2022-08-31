from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())

books = defaultdict(int)

for _ in range(N):
    books[input().strip()] += 1

# value값 기준으로 정렬
books = sorted(books.items(), key=lambda item:item[1], reverse=True)

# 겹치는 value값들 있을 때 처리 위한 과정
# list에 책 이름 다 넣고
tops = []

for book in books:
    if books[0][1] == book[1]:
        tops.append(book[0])

# 정렬해서 제일 앞에 거 꺼내오기
tops.sort()
print(tops[0])
