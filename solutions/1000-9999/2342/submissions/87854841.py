INF = int(1e9)
cur_state = [[INF]*5 for _ in range(5)]
cur_state[0][0] = 0
command = list(map(int,input().split()))

def move_left_foot(new_state,left,right,c):
    if left == 0:
        new_state[c][right] = min(new_state[c][right],cur_state[left][right]+2)
    elif left == c:
        new_state[c][right] = min(new_state[c][right],cur_state[left][right]+1)
    elif left % 2 == c % 2:
        new_state[c][right] = min(new_state[c][right],cur_state[left][right]+4)
    else:
        new_state[c][right] = min(new_state[c][right],cur_state[left][right]+3)

def move_right_foot(new_state,left,right,c):
    if right == 0:
        new_state[left][c] = min(new_state[left][c],cur_state[left][right]+2)
    elif right == c:
        new_state[left][c] = min(new_state[left][c],cur_state[left][right]+1)
    elif right % 2 == c % 2:
        new_state[left][c] = min(new_state[left][c],cur_state[left][right]+4)
    else:
        new_state[left][c] = min(new_state[left][c],cur_state[left][right]+3)    

for c in command:
    if c == 0: break
    new_state = [[INF]*5 for _ in range(5)]
    for left in range(5):
        for right in range(5):
            if cur_state[left][right] >= INF: continue
            if c != right: move_left_foot(new_state,left,right,c)
            if c != left: move_right_foot(new_state,left,right,c)
    cur_state = new_state

answer = INF

for i in range(5):
    for j in range(5):
        answer = min(answer,cur_state[i][j])

print(answer)