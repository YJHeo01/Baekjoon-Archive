import sys

input = sys.stdin.readline

n = int(input())

A,B,C,D = [],[],[],[]

for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a); B.append(b); C.append(c); D.append(d)

C.sort(); D.sort()

max_D,min_D = D[-1],D[0]

def search_C_min_idx(sum_A_B_maxD,C):
    left, right = 0,n-1
    ret_value = 0
    while left <= right:
        mid = (left+right) // 2
        if sum_A_B_maxD + C[mid] < 0:
            ret_value = mid
            left = mid + 1
        else:
            right = mid - 1
    return ret_value

def search_C_max_idx(sum_A_B_minD,C):
    left, right = 0,n-1
    ret_value = n-1
    while left <= right:
        mid = (left+right) // 2
        if sum_A_B_minD + C[mid] > 0:
            ret_value = mid
            right = mid - 1
        else:
            left = mid + 1
    return ret_value

def search_D_left(sum_A_B_C,D):
    left,right = 0,n-1
    ret_value = 0
    while left <= right:
        mid = (left+right) // 2
        if sum_A_B_C + D[mid] >= 0:
            ret_value = mid
            right = mid - 1
        else:
            left = mid + 1
    return ret_value

def search_D_right(sum_A_B_C,D):
    left,right = 0,n-1
    ret_value = n-1
    while left <= right:
        mid = (left+right) // 2
        if sum_A_B_C + D[mid] <= 0:
            ret_value = mid
            left = mid + 1
        else:
            right = mid - 1
    return ret_value

answer = 0

for A_idx in range(n):
    for B_idx in range(n):
        sum_A_B = A[A_idx] + B[B_idx]
        C_min_idx = search_C_min_idx(sum_A_B+max_D,C)
        C_max_idx = search_C_max_idx(sum_A_B+min_D,C)  + 1
        for C_idx in range(C_min_idx,C_max_idx):
            sum_A_B_C = sum_A_B + C[C_idx]
            left, right = 0,n-1
            if sum_A_B_C >= 0:
                right = search_D_right(sum_A_B_C,D)
            else:
                left = search_D_left(sum_A_B_C,D)
            while left <= right:
                D_idx = (left+right) // 2
                if sum_A_B_C + D[D_idx] > 0:
                    right = D_idx - 1
                elif sum_A_B_C + D[D_idx] < 0:
                    left = D_idx + 1
                else:
                    answer += 1
                    break

print(answer)