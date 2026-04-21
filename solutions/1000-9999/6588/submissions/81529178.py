import sys

input = sys.stdin.readline

def main():
    INF = 1000001
    prime = [True] * (INF)
    prime[0],prime[1],prime[2] = False,False
    prime_list = []
    answer = [[0]*2 for _ in range(INF)]
    for i in range(3,INF):
        if prime[i] == True:
            prime_list.append(i)
            for j in range(i+i,INF,i):
                prime[j] = False
        elif i % 2 == 0:
            for value in prime_list:
                if prime[i - value] == True:
                    answer[i] = [value,i-value]
                    break
    while True:
        n = int(input())
        if n == 0: break
        if answer[n][0] == 0:
            print("Goldbach's conjecture is wrong.")
            continue
        print(str(n) + " = " + str(answer[n][0]) + " + " + str(answer[n][1]))
    
if __name__ == "__main__":
    main()