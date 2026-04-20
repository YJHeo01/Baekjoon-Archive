def main():
    s = list(input())
    length = len(s)
    plus_value = 0
    while True:
        left, right = plus_value, length-1
        while left <= right:
            if s[left] != s[right]: break
            left += 1; right -= 1
        if left > right: break
        plus_value += 1
    answer = length + plus_value
    print(answer)    

if __name__ == "__main__":
    main()