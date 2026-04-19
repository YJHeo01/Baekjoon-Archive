def main():
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    answer = 0
    for i in range(1,n):
        if (array[i] - array[0]) <= k * i:
            answer += k * i - (array[i]-array[0])
        else:
            answer += ((array[i]-array[0]) - k * i) * i
            array[0] += (array[i]-array[0]) - k * i
    print(answer)

if __name__ == "__main__":
    main()