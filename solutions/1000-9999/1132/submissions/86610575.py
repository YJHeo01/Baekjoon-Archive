def main():
    n = int(input())
    value = {}
    cant_zero = set({})
    for _ in range(n):
        s = list(input())
        cant_zero.add(s[0])
        num = 1
        while s:
            alpha = s.pop()
            if alpha in value:
                value[alpha] += num
            else:
                value[alpha] = num
            num *= 10
    if len(value) == 10:
        zero = 'A'
        for i in list("ABCDEFGHIJ"):
            if i not in cant_zero:
                zero = i
                break
        for i in value:
            if i in cant_zero: continue
            if value[zero] >= value[i]:
                zero = i
        value[zero] = 0
    value = sorted(value.values())
    value.reverse()
    tmp = 9

    answer = 0
    for i in value:                                                                       
        answer += i * tmp
        tmp -= 1
    print(answer)

if __name__ == "__main__":
    main()