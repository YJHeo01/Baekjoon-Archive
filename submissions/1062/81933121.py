import sys
from itertools import combinations

input = sys.stdin.readline

data = ['b', 'd','e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
anta_tica = {'a','n','t','i','c'}

def main():
    n,k = map(int,input().split())
    if k < 5:
        print(0)
        return
    answer = 0
    word_list = get_word_list(n)
    study_case_list = list(combinations(data,k-5))
    for study_case in study_case_list:
        study_case = set(study_case)
        
        answer = max(answer,get_possible_read_word_cnt(word_list,study_case.union(anta_tica),n))
    print(answer)

def get_word_list(n):
    word_list = []
    for _ in range(n):
        tmp = list(input().rstrip())
        for _ in range(4):
            tmp.pop()
        word_list.append(tmp[4:])
    return word_list

def get_possible_read_word_cnt(word_list,possible_read,n):
    ret_value = n
    for word in word_list:
        for c in word:
            if c not in possible_read:
                ret_value -= 1
                break
    return ret_value

if __name__ == "__main__":
    main()