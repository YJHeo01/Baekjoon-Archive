def main():
    n = list(input())
    n.sort(reverse=True)
    for i in n:
        print(i,end="")

if __name__ == "__main__":
    main()