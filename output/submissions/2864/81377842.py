def main():
    a,b = input().split()
    min_a, min_b = "",""
    for i in a:
        if i == '6':
            i = '5'
        min_a += i
    for i in b:
        if i == '6':
            i = '5'
        min_b += i
    max_a, max_b = "", ""
    for i in a:
        if i == '5':
            i = '6'
        max_a += i
    for i in b:
        if i == '5':
            i = '6'
        max_b += i
    print(int(min_a)+int(min_b),int(max_a)+int(max_b))

if __name__ == "__main__":
    main()