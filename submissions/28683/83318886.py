import math

def main():
    n = int(input())
    if int(math.sqrt(n)) - math.sqrt(n) == 0:
        print(-1)
        return
    answer = 0
    for i in range(1,int(math.sqrt(n/2)+1)):
        j = n - i * i
        if math.sqrt(j) - int(math.sqrt(j)) == 0: answer += 1

    for i in range(1,int(math.sqrt(n))+1):
        if n % i != 0: continue
        if ((i+(n//i))%2 == 0 and i != n // i): answer += 1
    print(answer)

if __name__ == "__main__":
    main()