def main():
    left, right = map(int,input().split())
    if left > right: left, right = right, left
    x,y = map(int,input().split())
    if y < 0 or y >= abs(x):
        print("Unknwon Number")
        return
    answer = (left // x) * x + y
    if answer < left: answer += abs(x)
    if answer > right or answer + abs(x) <= right:
        print("Unknwon Number")
    else:
        print(answer)

if __name__ == "__main__":
    main()