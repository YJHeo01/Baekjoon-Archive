import sys

input = sys.stdin.readline

def main():
    t = int(input().rstrip())
    A,B,C,D = [],[],[],[]
    for _ in range(t):
        a,b,c,d = map(int,input().split())
        A.append(a); B.append(b); C.append(c); D.append(d)
    C.sort(); D.sort()
    answer = 0
    for a_idx in range(t):
        for b_idx in range(t):
            c_idx, d_idx = 0,t-1
            sum_value = A[a_idx] + B[b_idx] + C[c_idx] + D[d_idx]
            while True:
                if sum_value > 0:
                    if d_idx == 0: break
                    sum_value -= D[d_idx]
                    d_idx -= 1
                    sum_value += D[d_idx]
                elif sum_value < 0:
                    if c_idx == t-1: break
                    sum_value -= C[c_idx]
                    c_idx += 1
                    sum_value += C[c_idx]
                else:
                    answer += 1
                    if d_idx == 0 or c_idx == t-1: break
                    sum_value -= C[c_idx]; sum_value -= D[d_idx]
                    c_idx += 1; d_idx -= 1
                    sum_value += C[c_idx]; sum_value += D[d_idx]
    print(answer)

if __name__ == "__main__":
    main()