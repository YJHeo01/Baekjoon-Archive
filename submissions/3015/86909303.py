import sys

input = sys.stdin.readline

def main():
    n = int(input())
    stack = []
    answer = 0
    for _ in range(n):
        right = int(input())
        while stack:
            left = stack.pop()
            answer += 1
            if left >= right:
                stack.append(left)
                break
        stack.append(right)
    stack_length = len(stack)
    answer += stack_length-1
    print(answer)

if __name__ == "__main__":
    main()