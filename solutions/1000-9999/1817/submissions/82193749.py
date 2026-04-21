n,m = map(int,input().split())

if n == 0:
    print(0)
    exit(0)

books = list(map(int,input().split()))

weight = 0
answer = 1

for book in books:
    if weight + book > m:
        answer += 1
        weight = book
    else:
        weight += book

print(answer)