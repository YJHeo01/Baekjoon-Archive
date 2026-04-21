def main():
    left, right = map(int,input().split())
    x,y = map(int,input().split())
    answer = (left // x) * x + y
    if answer < left: answer += abs(x)
    if answer > right or answer + abs(x) <= right:
        print("Unknwon Number")
    else:
        print(answer)

if __name__ == "__main__":
    main()