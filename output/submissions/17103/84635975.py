import sys

input = sys.stdin.readline

def main():
    prime = [True] * INF
    prime_list = []
    for i in range(2,INF):
        if prime[i] == True:
            prime_list.append(i)
            for j in range(i+i,INF,i):
                prime[j] = False
    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = 0
        for i in prime_list:
            if i * 2 > n: break
            if prime[n-i] == True: answer += 1
        print(answer)

if __name__ == "__main__":
    INF = 1000001
    main()