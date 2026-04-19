def main():
    prime = [True] * INF
    prime_list = []
    for i in range(2,INF):
        if prime[i] == True:
            prime_list.append(i)
            for j in range(i,INF,i):
                prime[j] = False
    global length
    length = len(prime_list)
    t = int(input())
    for _ in range(t):
        n = int(input())
        answer = 0
        for i in range(1,length):
            if prime_list[i] * 2 > n:
                break
            answer += binary_search(prime_list,i,n)
        print(answer)

def binary_search(prime_list,left_idx,target):
    left, right = left_idx, length - 1
    while left <= right:
        mid = (left+right) // 2
        if prime_list[left_idx] + prime_list[mid] > target:
            right = mid - 1
        elif prime_list[left_idx] + prime_list[mid] < target:
            left = mid + 1
        else:
            return 1
    return 0
    
if __name__ == "__main__":
    INF = 1000001
    main()