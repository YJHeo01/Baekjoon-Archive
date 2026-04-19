#그리디
#가장 저렴한 수를 이용해서 가장 긴 자리 방 번호를 만든 후, 첫 자리 수부터 마지막 자리 수까지 그리디하게 값을 변경

def main():

    n = int(input())

    if n == 1: # n=1인 경우, 0만 만들수 있다.
        print(0)
        return

    price = list(map(int,input().split()))

    m = int(input())

    first_num_price = min(price[1:]) #첫 자리 수를 정하기 위함, 첫 자리 수로는 0이 들어갈 수 없음
    first_num = -1

    for i in range(n-1,0,-1):
        if first_num_price == price[i]:
            first_num = i
            break
    

    if first_num_price > m: #0을 제외한 수를 구매하지 못하는 경우, 0만 출력할 수 있다.
        print(0)
        exit(0)

    answer = []

    answer.append(first_num)

    m -= first_num_price

    min_price = min(price)

    for i in range(n-1,-1,-1): #가장 저렴한 수를 구함
        if min_price == price[i]:
            min_price_num = i
            break

    digit = 1

    while True: #가장 긴 숫자를 만들어줌
        if min_price > m:
            break
        digit += 1
        m -= min_price
        answer.append(min_price_num)

    for i in range(digit): #그리디하게 가장 큰 값을 만들어줌
        for num in range(n-1,0,-1):
            if answer[i] >= num or m >= price[num] - price[answer[i]]: 
                m -= (price[num] - price[answer[i]])
                answer[i] = num
                break

    for i in answer:
        print(i,end="")

if __name__ == "__main__":
    main()