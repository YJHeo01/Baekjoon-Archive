import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))


q = int(input())

for _ in range(q):
    i,j,k = map(int,input().split())
    a_left,a_right = 0,i-1
    finish = False
    while a_left <= a_right:
        a_mid = (a_left+a_right) // 2
        b_left, b_right = 0,j-1
        b_cnt = 0
        while b_left <= b_right:
            b_mid = (b_left+b_right) // 2
            if b[b_mid] < a[a_mid]:
                b_cnt = b_mid + 1
                b_left = b_mid + 1
            else:
                b_right = b_mid - 1
        rank = a_mid + b_cnt + 1
        if rank > k:
            a_right = a_mid - 1
        elif rank < k:
            a_left = a_mid + 1
        else:
            print(1,a_mid+1)
            finish = True
            break
    if finish: continue
    b_left,b_right = 0,j-1
    while b_left <= b_right:
        b_mid = (b_left+b_right) // 2
        a_left, a_right = 0,j-1
        a_cnt = 0
        while a_left <= a_right:
            a_mid = (a_left+a_right) // 2
            if a[a_mid] < b[b_mid]:
                a_cnt = a_mid + 1
                a_left = a_mid + 1
            else:
                a_right = a_mid - 1
        rank = b_mid + a_cnt + 1
        if rank > k:
            b_right = b_mid - 1
        elif rank < k:
            b_left = b_mid + 1
        else:
            print(2,b_mid+1)
            finish = True
            break