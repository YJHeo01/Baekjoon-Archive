def main():
    s = input()
    ucpc = ['U','C','P','C']
    idx = 0
    for c in s:
        if c == ucpc[idx]:
            idx += 1
        if idx >= 4:
            break
    if idx >= 4:
        print("I love UCPC")
    else:
        print("I hate UCPC")

if __name__ == "__main__":
    main()