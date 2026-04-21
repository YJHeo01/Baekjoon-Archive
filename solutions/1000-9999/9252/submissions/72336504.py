str1 = [0] + list(input())
str2 = [0] + list(input())
    
len_str1 = len(str1) 
len_str2 = len(str2)

dp = [[0]*len_str2 for _ in range(len_str1)]

for i in range(1,len_str1):
    for j in range(1,len_str2):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

x,y = len_str1-1, len_str2-1
answer1 = dp[x][y]
answer2 = []

while True:
    if dp[x][y] == 0:
        break
    if dp[x-1][y] == dp[x][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    else:
        answer2.append(str1[x])
        x -= 1; y -= 1

print(answer1)

if answer1 != 0:
    answer2.reverse()
    for c in answer2:
        print(c,end="")
