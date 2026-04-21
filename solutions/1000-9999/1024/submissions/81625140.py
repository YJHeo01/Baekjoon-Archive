n,l = map(int,input().split())

for length in range(l,101):
    tmp = n // length
    tmp_sum = tmp * length + (length * (length-1)) // 2
    while True:
        if tmp_sum < n or tmp < 0:
            break
        if tmp_sum == n:
            for i in range(length):
                print(tmp+i,end=" ")
            exit(0)

        tmp -= 1
        tmp_sum -= length

print(-1)