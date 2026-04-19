def main():
    answer = 0
    tmp = 0
    for _ in range(10):
        tmp += int(input())
        if abs(100-answer) >= abs(100-tmp):
            answer = tmp
    print(answer)

if __name__ == "__main__":
    main()