import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        x,y = map(int,input().split())
        tmp = y-x
        answer = 0
        max_move_size = 0
        while True:
            answer += 1
            if answer % 2 == 1: max_move_size += 1
            tmp -= max_move_size
            if tmp <= 0:break
        print(answer)

if __name__ == "__main__":
    main()