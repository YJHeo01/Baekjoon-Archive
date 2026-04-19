from collections import deque

def main():
    n = int(input())
    answer = 0
    array = deque(sorted(map(int,input().split())))
    if n % 2 == 1:
        answer = array.pop()
    while array:
        left = array.popleft()
        right = array.pop()
        answer = max(answer,left+right)
    print(answer)

if __name__ == "__main__":
    main()