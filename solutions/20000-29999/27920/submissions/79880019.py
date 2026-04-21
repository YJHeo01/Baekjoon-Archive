def main():
    n = int(input())
    b = [0] * (n+1)
    value = 1
    idx = n // 2 + 1
    c = []
    while True:
        if value > n:
            break
        b[idx] = value
        c.append(idx)
        if value % 2 == 1:
            idx -= value
        else:
            idx += value
        value += 1
    print('YES')
    print(*b[1:])
    print(*c)

if __name__ == "__main__":
    main()