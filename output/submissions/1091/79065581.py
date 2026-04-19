def main():
    p = list(map(int,input().split()))
    s = list(map(int,input().split()))
    visited = [-1] * (3**n)
    idx = convert_idx(p)
    visited[idx] = 0
    dfs(visited,p,s)
    target_card = get_target_card(n)
    target_idx = convert_idx(target_card)
    answer = visited[target_idx]
    print(answer)

def dfs(visited,cur_card,s):
    next_card = get_next_card(cur_card,s)
    next_idx = convert_idx(next_card)
    if visited[next_idx] == -1:
        cur_idx = convert_idx(cur_card)
        visited[next_idx] = visited[cur_idx] + 1
        dfs(visited,next_card,s)

def convert_idx(card):
    idx = 0
    for i in range(n):
        idx += card[i] * (3**i)
    return idx

def get_next_card(cur_card,s):
    next_card = [0] * n
    for i in range(n):
        next_card[s[i]] = cur_card[i]
    return next_card

def get_target_card(n):
    card = []
    for i in range(n):
        card.append(i%3)
    return card

if __name__ == "__main__":
    n = int(input())
    main()