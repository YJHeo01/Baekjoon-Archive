def main():
    p = list(map(int,input().split()))
    s = list(map(int,input().split()))
    answer = solution(p,p,s)
    if answer >= INF: answer = -1
    print(answer)

def solution(start_card,cur_card,s):
    if check_target_card(cur_card) == True:
        return 0
    next_card = get_next_card(cur_card,s)
    if check_same_card(start_card,next_card) == True: return INF
    return solution(start_card,next_card,s) + 1

def check_target_card(cur_card):
    for i in range(n):
        if cur_card[i] != i % 3:return False
    return True

def get_next_card(cur_card,s):
    next_card = [0] * n
    for i in range(n):
        next_card[s[i]] = cur_card[i]
    return next_card

def check_same_card(stard_card,cur_card):
    for i in range(n):
        if stard_card[i] != cur_card[i]: return False
    return True

if __name__ == "__main__":
    INF = int(1e9)
    n = int(input())
    main()