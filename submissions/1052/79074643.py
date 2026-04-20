def main():
    n,k = map(int,input().split())
    stack = []
    cnt = 0
    for i in range(24,-1,-1):
        if 2 ** i & n == 0:continue
        cnt += 1
        stack.append(i)
    answer = 0
    for _ in range(cnt-k):
        value_A = stack.pop()
        value_B = stack.pop()
        answer -= 2 ** value_A
        answer += 2 ** value_B
        stack.append(value_B+1)
    print(answer)

if __name__ == "__main__":
    main()