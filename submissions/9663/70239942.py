n = int(input())

def solution(queen_list,length):
    ret_value = 0
    okay = 1
    if length == n:
        return 1
    for next_column in range(n):
        if next_column in queen_list: # 세로로 공격
            continue
        for queen_row in range(length):
            if abs(length - queen_row) == abs(next_column - queen_list[queen_row]):
                okay = 0
                break
        if okay == 1:
            ret_value += solution(queen_list + [next_column],length+1)
        else:
            okay = 1
    return ret_value
answer = 0
for i in range(n):
    answer += solution([i],1)

print(answer)