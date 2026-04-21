n = int(input())
s = input()
answer = 'NO'
for i in range(4,n+1):
    if s[i-4:i] == "gori":
        answer = "YES"
print(answer)