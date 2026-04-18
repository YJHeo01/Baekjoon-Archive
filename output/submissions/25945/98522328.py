n = int(input())

arr = list(map(int,input().split()))

avg = sum(arr) // n

answer = 0

for i in arr:
    answer += min(abs(i-avg),abs(i-(avg+1)))
    
answer = answer //2 + answer % 2

print(answer)