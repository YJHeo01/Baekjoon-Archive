n = int(input())

num_list = list(map(int,input().split()))

num_list.sort()

answer = 0
for i in range(2,n):
    stop = 0
    for j in range(i-1):
        for k in range(j+1,i):
            if num_list[j]+num_list[k] == num_list[i]:
                answer+=1
                stop = 1
                break
        if stop == 1:
            break
            


print(answer)