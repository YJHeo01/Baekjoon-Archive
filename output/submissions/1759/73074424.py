l,c = map(int,input().split())

array = list(input().split())

array.sort()

def backtracking(idx_list):
    if len(idx_list) == l:
        consonant_cnt = 0
        vowel_cnt = 0
        for idx in idx_list:
            if array[idx] in ('a','e','i','o','u'):
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            for idx in idx_list:
                print(array[idx],end="")
            print()
        return
    for i in range(idx_list[-1]+1,c):
        backtracking(idx_list+[i])


for i in range(c-l+1):
    backtracking([i])