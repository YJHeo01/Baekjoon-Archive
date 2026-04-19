import sys

input = sys.stdin.readline

def main():
    prime_list = []
    prime_check = [True] * (100001)
    for i in range(2,100001):
        if prime_check[i]:
            prime_list.append(i)
            for j in range(i,100001,i):
                prime_check[j] = False
    length = len(prime_list)
    prime_cnt = [0] * length
    n = int(input())
    array = ['*'] + list(input().split())
    for i in range(n):
        tmp = abs(int(array[2*i+1]))
        if tmp == 0: continue
        for k in range(length):
            prime = prime_list[k]
            while True:
                if tmp % prime != 0: break
                if array[2*i] == '*': prime_cnt[k] += 1
                else: prime_cnt[k] -= 1
                tmp = tmp // prime
    answer = 'mint chocolate'
    for i in range(length):
        if prime_cnt[i] < 0:
            answer = 'toothpaste'
    print(answer)

if __name__ == "__main__":
    main()