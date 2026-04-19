def main():
    n = int(input())
    book = {}
    for _ in range(n):
        tmp = input()
        if tmp in book:
            book[tmp] += 1
        else:
            book[tmp] = 1
    answer = ''
    cnt = 0
    for name in book:
        if book[name] > cnt:
            answer = name
            cnt = book[name]
        elif book[name] == cnt:
            if answer > name:
                answer = name
    print(answer)

if __name__ == "__main__":
    main()