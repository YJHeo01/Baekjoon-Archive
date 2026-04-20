n = int(input())

num_list = list(map(int,input().split()))

m = int(input())


answer = 0
num_list.sort()
for i in range(n):
    if m > ((num_list[i]-answer)*(n-i)):
        m -= ((num_list[i]-answer)*(n-i))
        answer +=(num_list[i]-answer)
    else:
        if i == 0:
            continue
        answer += (m//(n-i))
        break
print(answer)