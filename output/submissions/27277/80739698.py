import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    left,right = 0,n-1
    answer = 0
    while True:
        if left >= right:
            answer += array[right]
            break
        answer += (array[right]-array[left])
        right -= 1; left += 1
    print(answer)

if __name__ == "__main__":
    main()