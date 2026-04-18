n,m = map(int,input().split())

answer = n // m

if n % m != 0: answer += 1

print(answer)