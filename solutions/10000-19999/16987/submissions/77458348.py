n = int(input())

hp = []
weight = []

for _ in range(n):
    a,b = map(int,input().split())
    hp.append(a)
    weight.append(b)

def get_new_hp(hp,weight,idx,attack_idx):
    new_hp = [0]*n
    for i in range(n):
        new_hp[i] = hp[i]
    new_hp[idx] -= weight[attack_idx]
    new_hp[attack_idx] -= weight[idx]
    return new_hp

def get_broken_egg_cnt(hp):
    ret_value = 0
    for i in range(n):
        if hp[i] <= 0:
            ret_value += 1
    return ret_value

def dfs(hp,weight,idx):
    if idx == n:
        return get_broken_egg_cnt(hp)
    if hp[idx] <= 0:
        return dfs(hp,weight,idx+1)
    ret_value = 0
    for attack_idx in range(n):
        if attack_idx == idx or hp[attack_idx] <= 0:
            continue
        new_hp = get_new_hp(hp,weight,idx,attack_idx)
        ret_value = max(ret_value,dfs(new_hp,weight,idx+1))
    if ret_value == 0:
        return get_broken_egg_cnt(hp)
    return ret_value

answer = dfs(hp,weight,0)

print(answer)