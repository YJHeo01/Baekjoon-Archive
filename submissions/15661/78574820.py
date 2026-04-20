import sys

sys.setrecursionlimit(10**6)

def main():
    global n
    n = int(input())
    array = get_array(n)
    link_score = init_link_score(array)
    answer = get_answer(array,[0],0,link_score)
    print(answer)

def get_array(n):
    array = []
    for _ in range(n): array.append(list(map(int,input().split())))
    return array

def init_link_score(array):
    ret_value = 0
    for i in range(1,n):
        for j in range(1,n):
            ret_value += array[i][j]
    return ret_value

def get_answer(array,A_member,A_score,B_score):
    ret_value = abs(A_score-B_score)
    last_start_member = A_member[-1]
    for A_new_member in range(last_start_member+1,n):
        change_A_score, change_B_score = change_score(array,A_member,A_new_member)
        new_A_score, new_B_score = A_score+ change_A_score, B_score - change_B_score
        ret_value = min(ret_value,get_answer(array,A_member+[A_new_member],new_A_score,new_B_score))
    return ret_value

def change_score(array,members,new_member):
    change_A_score = 0
    change_B_score = 0
    for member in range(n):
        tmp = array[member][new_member] + array[new_member][member]
        if member in members: change_A_score += tmp
        else: change_B_score += tmp
    return change_A_score,change_B_score

if __name__ == "__main__":
    main()