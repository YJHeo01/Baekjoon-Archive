import sys

input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        if m == 1:
            print("0 0")
            continue
        tmp = []
        for i in range(60):
            if 2 ** i & m != 0:
                tmp.append(i)
        if len(tmp) == 1:
            value = tmp.pop()
            for _ in range(2):
                tmp.append(value-1)
        tmp.reverse()
        while True:
            if len(tmp) == 2:
                break
            tmp.pop()
        print(tmp.pop(),end=" ")
        print(tmp.pop())

if __name__ == "__main__":
    main()