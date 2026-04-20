n,x = map(int,input().split())

blog = list(map(int,input().split()))

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + blog[i]

first_answer = 0
second_answer = 0

for i in range(x,n+1):
    tmp = prefix_sum[i] - prefix_sum[i-x]
    if tmp > first_answer:
        first_answer = tmp
        second_answer = 1
    elif tmp == first_answer:
        second_answer+=1

if first_answer == 0:
    print("SAD")
else:
    print(first_answer)
    print(second_answer)