import sys

input = sys.stdin.readline

n = int(input())

A,B,C,D = [],[],[],[]

for _ in range(n):
    value_a, value_b, value_c, value_d = map(int,input().split())
    A.append(value_a); B.append(value_b); C.append(value_c); D.append(value_d)

D.sort()

answer = 0

for A_idx in range(n):
    for B_idx in range(n):
        for C_idx in range(n):
            sum_A_B_C = A[A_idx] + B[B_idx] + C[C_idx]
            if D[-1] + sum_A_B_C < 0 or D[0] + sum_A_B_C > 0:
                continue
            left, right = 0,n-1
            while left <= right:
                D_idx = (left + right) // 2
                sum_A_B_C_D = sum_A_B_C + D[D_idx]
                if sum_A_B_C_D > 0:
                    right = D_idx - 1
                elif sum_A_B_C_D < 0:
                    left = D_idx + 1
                else:
                    answer += 1
                    break
print(answer)