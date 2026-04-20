n, l = map(int,input().split())

box = list(map(int,input().split()))

unstable = 0
sum_ = 0
if n == 1:
    print("unstable")
else : 
    for i in range(1,n):
        sum_ += box[i]
        sum__ = sum_ / (n-i)
        if box[i-1] - l >= sum__ or sum__ >= box[i-1] + l:
            unstable = 1
            break
    if unstable == 0 :
        print("stable")
    else: print("unstable")