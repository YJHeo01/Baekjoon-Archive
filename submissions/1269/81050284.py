def main():
    a_cnt, b_cnt = map(int,input().split())
    a = set(map(int,input().split()))
    b = set(map(int,input().split()))
    print(len((a|b)-(a&b)))

if __name__ == "__main__":
    main()