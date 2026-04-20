def main():
    while True:
        try:
            A,B = input().split()  
        except:
            break
        print(solution(list(A),list(B)))

def solution(A,B):
    len_A = len(A)
    len_B = len(B)
    B_idx = -1
    for A_idx in range(len_A):
        while True:
            B_idx += 1
            if B_idx == len_B: return "No"
            if A[A_idx] == B[B_idx]:
                break    
    return "Yes"

if __name__ == "__main__":
    main()