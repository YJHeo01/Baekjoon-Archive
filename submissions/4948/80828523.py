import math, sys

input = sys.stdin.readline

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
    prefix_sum = [0] * SIZE
    for i in range(1,SIZE):
        prefix_sum[i] = prefix_sum[i-1] + prime[i]
    while True:
        n = int(input())
        if n == 0:break
        print(prefix_sum[2*n]-prefix_sum[n])

if __name__ == "__main__":
    main()