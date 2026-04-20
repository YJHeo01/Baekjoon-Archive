while 1:
    answer = 'yes'
    n = input()
    if n == '0':
        break
    l = len(n)
    for i in range(l//2):
        if n[i] != n[l-1-i]:
            answer = 'no'
            break
    print(answer)