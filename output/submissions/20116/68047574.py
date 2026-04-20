n, l = map(int,input().split())

box = list(map(int,input().split()))

unstable = 0

if n == 1:
    print("stable")
else : 
    for i in range(1,n):
        sum_ = sum(box[i:])
        sum_ = sum_ / (n-1)
        if box[i-1] - l >= sum_ or sum_ >= box[i-1] + l:
            unstable = 1
            break
    if unstable == 0 :
        print("stable")
    else: print("unstable")