import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    answer_dna = ""
    hammingDistance = n * m
    s_list = [input().rstrip() for _ in range(n)]
    for i in range(m):
        alphabet_cnt = {'A':0,'C':0,'G':0,'T':0}
        for s in s_list:
            alphabet_cnt[s[i]] += 1
        next_char = 'A'
        for c in ['C','G','T']:
            if alphabet_cnt[c] > alphabet_cnt[next_char]:
                next_char = c
        answer_dna += next_char
        hammingDistance -= alphabet_cnt[next_char]
    print(answer_dna)
    print(hammingDistance)

if __name__ == "__main__":
    main()