import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        m = int(input())
        a = []
        for _ in range(m//10):
            a += list(map(int,input().split()))
        if m % 10 != 0: a += list(map(int,input().split()))
        sum_value = sum(a)
        biggest_value = max(a)
        tmp = 0
        num_list = []
        prefix_sum = [0] * (m+1)
        for i in range(m):
            prefix_sum[i+1] = prefix_sum[i] + a[i]
        for i in range(m):
            tmp += a[i]
            if tmp < biggest_value or sum_value % tmp != 0: continue
            if solution(prefix_sum,m,tmp):
                print(tmp)
                break

def solution(prefix_sum,m,length):
    cur = 0
    while True:
        if cur == m: return True
        left, right = cur+1 ,m
        next_node = cur
        while left <= right:
            mid = (left+right) // 2
            if prefix_sum[mid] - prefix_sum[cur] > length:
                right = mid - 1
            elif prefix_sum[mid] - prefix_sum[cur] < length:
                left = mid + 1
            else:
                next_node = mid
                break
        if next_node == cur: return False
        cur = next_node

if __name__ == "__main__":    
    main()