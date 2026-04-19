def main():
    n,m = map(int,input().split())
    j = int(input())
    left, right = 1,m
    answer = 0
    for _ in range(j):
        apple = int(input())
        if apple > right:
            dx = apple - right
        elif apple < left:
            dx = apple - left
        else:
            dx = 0
        answer += abs(dx)
        left += dx; right += dx
    print(answer)

if __name__ == "__main__":
    main()