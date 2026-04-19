def main():
    m = int(input())
    n = int(input())
    min_value = -1
    sum_value = 0
    for i in range(101):
        if i ** 2 > n:
            break
        if i ** 2 >= m:
            sum_value += i ** 2
            if min_value == -1: min_value = i ** 2
    if sum_value == 0:
        print(-1)
    else:
        print(sum_value)
        print(min_value)

if __name__ == "__main__":
    main()