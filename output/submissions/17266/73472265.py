n = int(input())
m = int(input())
array = list(map(int,input().split()))

answer_double = max(2*array[0],2*(n-array[m-1]))

for i in range(1,m):
    if answer_double < array[i] - array[i-1]:
        answer_double = array[i] - array[i-1]

print(answer_double//2+answer_double%2)