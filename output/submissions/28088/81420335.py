import sys

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    eung_Ae = [False] * n
    for _ in range(m):
        eung_Ae[int(input())] = True
    for _ in range(k):
        new_eung_Ae = [0] * n
        for i in range(n):
            if eung_Ae[i] == True:
                new_eung_Ae[(i+1)%n] += 1
                new_eung_Ae[(i-1)%n] += 1
        for i in range(n):
            if new_eung_Ae[i] == 1:
                eung_Ae[i] = True
            else:
                eung_Ae[i] = False
    answer = 0
    for i in range(n):
        if eung_Ae[i] == True:
            answer += 1
    print(answer)

if __name__ == "__main__":
    main()