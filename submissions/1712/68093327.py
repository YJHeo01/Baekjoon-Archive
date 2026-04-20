a, b, c = map(int,input().split())

if b > c:
    print("-1")
else : 
    answer =( a // (c-b) ) + 1

    if a % (c-b) != 0:
        answer += 1
    print(answer)