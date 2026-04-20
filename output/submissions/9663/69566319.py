import sys
sys.setrecursionlimit(10**6)


answer = 0

n = int(input())

size = n ** 2

point_list = [0] * size

for i in range(size):
    point_list[i] = i
def backtracking(n,queen_list,new_start_idx):
    global answer
    l = len(queen_list)
    if  l == n:
        answer += 1
        return
    for i in range(new_start_idx,size):
        if point_list[i] in queen_list:
            continue
        if queen_list == []:
            queen_list.append(point_list[i])
            backtracking(n,queen_list,i+1)
            queen_list.pop()
        else:
            p_x, p_y = point_list[i]//n, point_list[i] % n
            stop = 0
            for queen in queen_list:
                q_x, q_y = queen//n, queen % n
                if (q_x == p_x) or (q_y == p_y) or ((q_x-p_x) == -(q_y-p_y)) or ((q_x-p_x) == (q_y-p_y)):
                    stop = 1
                    break
            if stop == 0 and (size- i) + l >= n:
                queen_list.append(point_list[i])
                backtracking(n,queen_list,i+1)
                queen_list.pop()




backtracking(n,[],0)

print(answer)