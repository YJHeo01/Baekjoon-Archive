from collections import deque
from itertools import permutations
import sys

input = sys.stdin.readline

INF = int(1e9)

def main():
    inning_result = get_inning_result(n)
    player_idx_list = get_player_idx_list()
    test_case_list = list(permutations(player_idx_list,8))
    answer = solution(test_case_list,inning_result)
    print(answer)

def get_inning_result(n):
    ret_value = []
    for _ in range(n): ret_value.append(list(map(int,input().split())))
    return ret_value

def get_player_idx_list():
    player_idx_list = []
    for i in range(1,9): player_idx_list.append(i)
    return player_idx_list

def solution(test_case_list,inning_result):
    answer = 0
    for line_up in test_case_list:
        line_up = list(line_up)
        line_up = line_up[:3] + [0] + line_up[3:]
        answer = max(answer,baseball(inning_result,line_up))
    return answer

def baseball(inning_result,line_up):
    score = 0
    idx = 0
    for inning in range(n):
        out = 0
        base = deque([0,0,0])
        while True:
            result = inning_result[inning][line_up[idx]]
            idx = (idx+1) % 9
            if result == 0: 
                out += 1
                if out == 3: break
                continue
            base.append(1)
            for _ in range(result): score += base.popleft()
            for _ in range(result-1): base.append(0)
    return score
            
if __name__ == "__main__":
    n = int(input())
    main()