import sys
from itertools import combinations

input = sys.stdin.readline

possible_read = {'a':False,'b':False,'c':False,'d':False,'e':False,'f':False,'g':False,
                'h':False, 'i':False, 'j':False, 'k':False, 'l':False, 'n':False, 'm':False, 
                'o':False, 'p':False, 'q':False, 'r':False, 's':False, 't':False, 'u':False, 
               'v':False, 'w':False, 'x':False, 'y':False, 'z':False}
data = ['b', 'd','e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
anta_tica = ['a','n','t','i','c']

def main():
    n,k = map(int,input().split())
    if k < 5:
        print(0)
        return
    answer = 0
    word_list = get_word_list(n)
    study_case_list = list(combinations(data,k-5))
    study_alphabet(possible_read,anta_tica)
    for study_case in study_case_list:
        study_alphabet(possible_read,study_case)
        answer = max(answer,get_possible_read_word_cnt(word_list,possible_read,n))
        init_possible_read(possible_read,study_case)
    print(answer)

def get_word_list(n):
    word_list = []
    for _ in range(n):
        tmp = list(input().rstrip())
        for _ in range(4):
            tmp.pop()
        word_list.append(tmp[4:])
    return word_list

def study_alphabet(possible_read,alphabet):
    for c in alphabet:
        possible_read[c] = True
    return

def get_possible_read_word_cnt(word_list,possible_read,n):
    ret_value = n
    for word in word_list:
        for c in word:
            if possible_read[c] == False:
                ret_value -= 1
                break
    return ret_value

def init_possible_read(possible_read,alphabet):
    for c in alphabet:
        possible_read[c] = False
    return

if __name__ == "__main__":
    main()