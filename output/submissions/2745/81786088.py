def main():
    n,b = input().split()
    b = int(b)
    answer = 0
    for value in n:
        answer *= b
        if value.isdigit() == True:
            answer += int(value)
        else:
            answer += (10+ord(value)-ord('A'))
    print(answer)

if __name__ == "__main__":
    main()