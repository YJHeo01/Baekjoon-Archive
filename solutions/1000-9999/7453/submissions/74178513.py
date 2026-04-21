import sys

input = sys.stdin.readline

n = int(input())

A,B,C,D = [],[],[],[]

for _ in range(n):
    value_a, value_b, value_c, value_d = map(int,input().split())
    A.append(value_a); B.append(value_b); C.append(value_c); D.append(value_d)

C.sort(); D.sort()

answer = 0
for A_idx in range(n):
    for B_idx in range(n):
        sum_A_B = A[A_idx] + B[B_idx]
        C_idx = 0; D_idx = n-1
        while True:
            if C_idx >= n or D_idx < 0:
                break
            sum_A_B_C_D = sum_A_B + C[C_idx] + D[D_idx]
            if sum_A_B_C_D > 0:
                D_idx -= 1
            elif sum_A_B_C_D < 0:
                C_idx += 1
            else:
                answer += 1
                C_idx += 1
                D_idx -= 1

print(answer)