import sys

input = sys.stdin.readline

def main():
    n = int(input())
    car = {}
    for i in range(n):
        car[input().rstrip()] = i
    answer = 0
    for i in range(n):
        if i < car[input().rstrip()]:
            answer += 1
    print(answer)

if __name__ == "__main__":
    main()