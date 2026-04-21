#https://github.com/YJHeo01

n = int(input())

crime_score = list(map(int,input().split()))

R_array = []

for _ in range(n):
    R_array.append(list(map(int,input().split())))

mafia = int(input())

def game_afternoon(night,kill_member,score):
    if len(kill_member) == n:
        return night
    next_kill_member = kill_member[0]
    for i in range(n):
        if i in kill_member:
            continue
        if score[i] >= score[next_kill_member]:
            if score[i] > score[next_kill_member] or next_kill_member > i:
                next_kill_member = i
    if next_kill_member == kill_member[0]:
        return night
    else:
        return game_night(night,kill_member + [next_kill_member], score)


def game_night(night,kill_member,score):
    if len(kill_member) == n:
        return night
    ret_value = night
    for i in range(n):
        if i in kill_member:
            continue
        for j in range(n):
            score[j] += R_array[i][j]
        ret_value = max(ret_value,game_afternoon(night+1,kill_member+[i],score))
        for j in range(n):
            score[j] -= R_array[i][j]
    return ret_value


if n % 2 == 0:
    answer = game_night(0,[mafia],crime_score)
else:
    answer = game_afternoon(0,[mafia],crime_score)

print(answer)