def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = list(map(int,input().split()))
    zero_exist = False
    answer = 1
    for i in range(n):
        if abs(b[i]-a[i]) % x[i] != 0:
            print(-1)
            return
        original_value = abs(b[i]-a[i]) // x[i]
        if original_value == 0:
            zero_exist = True
            continue
        if original_value > answer:
            answer, original_value = original_value, answer
        left, right = answer, original_value
        while True:
            mod_value = left % right
            if mod_value == 0:
                break
            left = right
            right = mod_value
        answer = answer // right
        answer *= original_value
    if answer % 2 == 1 and zero_exist:
        answer *= 2
    print(answer)

if __name__ == "__main__":
    main()