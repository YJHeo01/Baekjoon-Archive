import sys

input = sys.stdin.readline

def main():
    n = int(input())
    answer = 0
    for _ in range(n):
        word = list(input().rstrip())
        stack = []
        while word:
            c = word.pop()
            if stack == [] or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        if stack == []:answer += 1
    print(answer)

if __name__ == "__main__":
    main()