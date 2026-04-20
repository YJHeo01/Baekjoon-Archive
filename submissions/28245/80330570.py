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
            print(value-1, value-1)
            continue
        tmp.reverse()
        plus_value = 2 ** tmp[1]
        minus_value = 0
        while True:
            if len(tmp) == 2:
                break
            value = tmp.pop()
            minus_value += value
            plus_value -= value
        if plus_value < minus_value:
            tmp[1] += 1
        print(tmp.pop(),end=" ")
        print(tmp.pop())

if __name__ == "__main__":
    main()