import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        solution()

def solution():
    s = list(input().rstrip())
    idx_list = get_idx_list(s)
    get_answer(idx_list)

def get_idx_list(s):
    idx_list = [[] for _ in range(26)]
    length = len(s)
    for i in range(length):
        idx = ord(s[i]) - ord('a')
        idx_list[idx].append(i)
    return idx_list

def get_answer(idx_list):
    k = int(input())
    max_value, min_value = -1,10001
    for i in range(26):
        alphabet_idx_list = idx_list[i]
        alphabet_cnt = len(alphabet_idx_list)
        if k > alphabet_cnt: continue
        for left in range(alphabet_cnt-k+1):
            right = left + k - 1
            str_length = (alphabet_idx_list[right]-alphabet_idx_list[left]) + 1
            max_value = max(str_length,max_value)
            min_value = min(min_value,str_length)    
    if max_value <= -1:print(-1)
    else:print(min_value,max_value)
    
if __name__ == "__main__":
    main()