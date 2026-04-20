import math

def main():
    SIZE = int(123456 * 2 + 1)
    prime = [True] * SIZE
    prime[0], prime[1] = False,False
    for i in range(2,int(math.sqrt(SIZE))+1):
        if prime[i] == False:continue
        value = i
        while True:
            value += i
            if value >= SIZE: break
            prime[value] = False
    while True:
        n = int(input())
        if n == 0:break
        answer = 0
        for i in range(n+1,2*n+1):
            if prime[i] == True:answer += 1
        print(answer)

if __name__ == "__main__":
    main()