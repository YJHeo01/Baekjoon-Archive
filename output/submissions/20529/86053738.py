def main():
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        array = list(input().split())
        
        key_value = dict([])
      
        for i in array:
            if i in key_value:
                key_value[i] += 1
            else:
                key_value[i] = 1

        answer = 100
        one_cnt, two_cnt = [], []

        for key in key_value:
            if key_value[key] == 1:
                one_cnt.append(key)
            elif key_value[key] == 2:
                two_cnt.append(key)
                one_cnt.append(key)
            else:
                answer = 0
        
        for mbti_A in two_cnt:
            for mbti_B in one_cnt:
                if mbti_A == mbti_B: continue
                tmp = 0
                for i in range(4):
                    if mbti_A[i] != mbti_B[i]: tmp += 2
                answer = min(answer,tmp)
        
        for mbti_A in one_cnt:
            for mbti_B in one_cnt:
                if mbti_A == mbti_B: continue
                for mbti_C in one_cnt:
                    if mbti_A == mbti_C or mbti_B == mbti_C: continue
                    tmp = 0
                    for i in range(4):
                        if mbti_A[i] != mbti_B[i]: tmp += 1
                        if mbti_B[i] != mbti_C[i]: tmp += 1
                        if mbti_C[i] != mbti_A[i]: tmp += 1
                    answer = min(answer,tmp)
        print(answer)

if __name__ == "__main__":
    main()