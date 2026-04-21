import sys

input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    print(*solution(array,n,k))

def solution(array,n,k):
    cnt = 0
    for last in range(n-1,-1,-1):
        idx = last
        for i in range(last):
            if array[i] > array[idx]:
                idx = i
        if idx != last:
            cnt += 1
            array[idx], array[last] = array[last], array[idx]
        if cnt == k:
            return array
    return [-1]

if __name__ == "__main__":
    main()