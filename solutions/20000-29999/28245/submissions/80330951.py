import sys

input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        tmp = []
        for i in range(60):
            if 2 ** i & m != 0:
                tmp.append(i)
        if len(tmp) == 1:
            value = tmp.pop()
            if value == 0:
                print("0 0")
            else:
                print(value,value)
            continue
        tmp.reverse()
        plus_value = 2 ** tmp[1]
        minus_value = 0
        while True:
            if len(tmp) == 2:
                break
            value = tmp.pop()
            minus_value += 2 ** value
            plus_value -= 2 ** value
        if plus_value < minus_value:
            tmp[1] += 1
        print(tmp.pop(),end=" ")
        print(tmp.pop())

if __name__ == "__main__":
    main()