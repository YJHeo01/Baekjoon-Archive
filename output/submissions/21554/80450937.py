def main():
    n = int(input())
    array = list(map(int,input().split()))
    cnt = 0
    answer = []
    for right in range(n-1,-1,-1):
        biggest_idx = -1
        biggest_value = -1
        for left in range(right+1):
            if array[left] > biggest_value:
                biggest_value = array[left]
                biggest_idx = left
        if biggest_idx == right: continue
        cnt += 1
        answer.append((biggest_idx+1,right+1))
        array[biggest_idx],array[right] = array[right], array[biggest_idx]
    print(cnt)
    for a,b in answer:
        print(a,b)

if __name__ == "__main__":
    main()