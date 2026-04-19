n = int(input())

array = sorted([list(map(int,input().split())) for _ in range(n)])

answer = 0

for a,b in array:
    if answer < a: answer = a
    answer += b
    
print(answer)