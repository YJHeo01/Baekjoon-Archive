def main():
    n,l,r,x = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort()
    answer = 0
    for bit in range(1,2**n):
        hard_idx = -1
        easy_idx = -1
        sum_score = 0
        for i in range(n):
            if (bit >> i) & 1:
                sum_score += array[i]
                if easy_idx == -1: easy_idx = i
                hard_idx = i
        if sum_score < l or sum_score > r or (array[hard_idx] - array[easy_idx]) < x: continue
        answer += 1
    print(answer)
        

if __name__  == "__main__":
    main()