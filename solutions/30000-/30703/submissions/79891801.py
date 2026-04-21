def main():
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = list(map(int,input().split()))
    answer = solution(a,b,x)
    print(answer)

def solution(a,b,x):
    zero_exist, one_exist = False, False
    odd_max, even_max  = -1, -1
    for i in range(n):
        if b[i] == a[i]:
            even_max = max(even_max,0) 
            zero_exist = True
            continue
        if abs(b[i]-a[i]) % x[i] != 0:
            return -1
        tmp = abs(b[i]-a[i]) // x[i]
        if tmp % 2 == 1:
            odd_max = max(odd_max,tmp)
            if tmp == 1:
                one_exist = True
        else:
            even_max = max(even_max,tmp)

    if odd_max == -1:
        return even_max
    if even_max == -1:
        return odd_max
    if one_exist:
        return -1
    
    big,small = max(odd_max,even_max), min(odd_max,even_max)
    while True:
        mod_value = big % small
        if mod_value == 0:
            return even_max//small*odd_max
        big = small
        small = mod_value

if __name__ == "__main__":
    n = int(input())
    main()