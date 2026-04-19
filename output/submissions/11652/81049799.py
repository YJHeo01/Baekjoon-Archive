import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = {}
    for _ in range(n):
        value = input().rstrip()
        if value not in array:
            array[value] = 1
        else:
            array[value] += 1
    answer = 0
    cnt = 0
    for value in array:
        if array[value] > cnt:
            answer = int(value)
            cnt = array[value]
        elif array[value] == cnt:
            answer = min(answer,int(value))
    print(answer)

if __name__ == "__main__":
    main()