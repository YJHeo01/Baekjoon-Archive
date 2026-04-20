import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    title_list = get_title_list(n)
    solution(title_list,m)

def get_title_list(n):
    ret_value = []
    for _ in range(n):
        title, score = input().split()
        ret_value.append((title,int(score)))
    return ret_value

def solution(title_list,m):
    for _ in range(m):
        value = int(input())
        answer = get_answer(title_list,value)
        print(answer)

def get_answer(title_list,value):
    for title, score in title_list:
        if score >= value: return title

if __name__ == "__main__":
    main()