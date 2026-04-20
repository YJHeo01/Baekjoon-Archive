import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    house = list(map(int,input().split()))
    house.sort()
    answer = house[0]
    mid = sum(house) / n
    for x in house[1:]:
        if abs(answer-mid) > abs(x - mid):
            answer = x
    print(answer)

if __name__ == "__main__":
    main()