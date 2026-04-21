import sys

input = sys.stdin.readline

def main():
    p = int(input())
    for _ in range(p):
        solution()

def solution():
    array = list(map(int,input().split()))
    answer = 0
    for start in range(2,12):
        min_value = array[start]
        for end in range(start,13):
            if array[start-1] >= array[end]:break
            min_value = min(array[end],min_value)
            if min_value > array[end+1]: answer += 1
    print(array[0],answer)

if __name__ == "__main__":
    main()