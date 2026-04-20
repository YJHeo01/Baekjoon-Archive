n = int(input())

num_list = list(map(int,input().split()))

money = int(input())


answer = 0
num_list.sort()
for i in range(n):
    if money > ((num_list[i]-answer)*(n-i)):
        money -= ((num_list[i]-answer)*(n-i))
        answer +=(num_list[i]-answer)
    else:
        if i == 0:
            continue
        answer += (money//i)
        break
print(answer)