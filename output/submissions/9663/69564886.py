answer = 0

def backtracking(n,queen_list,point_list):
    global answer
    if len(queen_list) == n:
        answer += 1
        return
    for point in point_list:
        if point in queen_list:
            continue
        if queen_list == []:
            queen_list.append(point)
            backtracking(n,queen_list,point_list)
            queen_list.pop()
        else:
            p_x, p_y = point//n, point % n
            stop = 0
            if point < queen_list[-1]:
                continue
            for queen in queen_list:
                q_x, q_y = queen//n, queen % n
                if (q_x == p_x) or (q_y == p_y) or ((q_x-p_x) == -(q_y-p_y)) or ((q_x-p_x) == (q_y-p_y)):
                    stop = 1
                    break
            if stop == 0:
                queen_list.append(point)
                backtracking(n,queen_list,point_list)
                queen_list.pop()


n = int(input())

size = n ** 2

num_list = [0] * size

for i in range(size):
    num_list[i] = i

backtracking(n,[],num_list)

print(answer)
