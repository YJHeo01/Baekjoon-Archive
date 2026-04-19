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
        left,right = 0,len(prime_list)-1
        answer_L = right
        while left <= right:
            mid = (left+right) // 2
            if prime_list[mid] * 2 <= n:
                answer_L = mid
                left = mid + 1
            else:
                right = mid - 1
        answer_R = answer_L
        while True:
            if prime_list[answer_L] + prime_list[answer_R] > n:
                answer_L -= 1
            elif prime_list[answer_L] + prime_list[answer_R] < n:
                answer_R += 1
            else:
                break
        print(prime_list[answer_L],prime_list[answer_R])
            
if __name__ == "__main__":
    main()