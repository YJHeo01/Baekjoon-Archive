def main():
    n = int(input())
    value = {}
    for _ in range(n):
        s = list(input())
        num = 1
        while s:
            alpha = s.pop()
            if alpha in value:
                value[alpha] += num
            else:
                value[alpha] = num
            num *= 10
    value = sorted(value.values())
    value.reverse()
    tmp = 9

    answer = 0
    for i in value:
        answer += i * tmp
        tmp -= 1
    print(answer)

if __name__ == "__main__":
    main()