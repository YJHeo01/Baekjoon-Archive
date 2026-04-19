import sys

input = sys.stdin.readline

def main():
    t = int(input().rstrip())
    A,B,C,D = [],[],[],[]
    for _ in range(t):
        a,b,c,d = map(int,input().split())
        A.append(a); B.append(b); C.append(c); D.append(d)
    AB, CD = [], []
    for i in range(t):
        for j in range(t):
            AB.append(A[i]+B[j])
            CD.append(C[i]+D[j])
    AB.sort(); CD.sort()
    left, right = 0,t * t - 1
    answer = 0
    while True:
        if left >= t * t or right < 0:break
        if AB[left] + CD[right] > 0:
            right -= 1
        elif AB[left] + CD[right] < 0:
            left += 1
        else:
            answer += 1
            right -= 1; left += 1
    print(answer)

if __name__ == "__main__":
    main()