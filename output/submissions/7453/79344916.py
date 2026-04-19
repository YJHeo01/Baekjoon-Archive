import sys

input = sys.stdin.readline

def main():
    n = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a,b,c,d = map(int,input().split())
        A.append(a); B.append(b); C.append(c); D.append(d)
    C.sort(); D.sort()
    answer = 0
    for idx_a in range(n):
        for idx_b in range(n):
            idx_c, idx_d = 0,n-1
            A_Bvalue = A[idx_a] + B[idx_b]
            while True:
                if idx_c >= n or idx_d < 0:break
                A_B_C_Dvlaue= A_Bvalue + C[idx_c] + D[idx_d]
                if A_B_C_Dvlaue > 0:
                    idx_d -= 1
                elif A_B_C_Dvlaue < 0:
                    idx_c += 1
                else:
                    answer += 1
                    idx_d -= 1
                    idx_c += 1
    print(answer)

if __name__ == "__main__":
    main()