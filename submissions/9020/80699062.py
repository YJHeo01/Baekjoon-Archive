import sys

input = sys.stdin.readline

def main():
    t = int(input())
    prime = [True] * 10001
    prime_list = []
    for i in range(2,10001):
        if prime[i] == True:
            prime_list.append(i)
            for j in range(i+i,10001,i):
                prime[j] = False
    for _ in range(t):
        n = int(input())
        left, right = 0,len(prime_list)-1
        answer_L, answer_R = 0,right
        while left <= right:
            if prime_list[right] + prime_list[left] > n:
                right -= 1
            elif prime_list[left] + prime_list[right] < n:
                left += 1
            else:
                if prime_list[answer_R] - prime_list[answer_L] > prime_list[right] - prime_list[left]:
                    answer_L, answer_R = left, right
                    left += 1; right -= 1
        print(prime_list[answer_L],prime_list[answer_R])

if __name__ == "__main__":
    main()