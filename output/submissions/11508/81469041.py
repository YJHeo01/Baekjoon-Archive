import sys

input = sys.stdin.readline

def main():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(int(input()))
    array.sort(reverse=True)
    answer = 0
    for i in range(n):
        if i % 3 == 2:continue
        answer += array[i]
    print(answer)

if __name__ == "__main__":
    main()