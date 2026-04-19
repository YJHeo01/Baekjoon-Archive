import sys

input = sys.stdin.readline

def main():
    c = int(input())
    position = [False] * 11
    for _ in range(c):
        S = [list(map(int,input().split())) for _ in range(11)]
        answer = backtracking(S,position,0,0)
        print(answer)


def backtracking(S,complete_position,player_idx,power):
    if player_idx == 11: return power
    ret_value = 0
    for position in range(11):
        if complete_position[position] or S[player_idx][position] == 0: continue
        complete_position[position] = True
        ret_value = max(ret_value,backtracking(S,complete_position,player_idx+1,power+S[player_idx][position]))
        complete_position[position] = False
    return ret_value

if __name__ == "__main__":
    main()