import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    v = int(input())
    tree = get_tree(v)
    global answer
    answer = 0
    for i in range(1,v+1):
        if len(tree[i]) >= 2:
            dfs(tree,[False] * (v+1),0,i)
            break
    print(answer)
    
def get_tree(v):
    tree = [[] for _ in range(v+1)]
    for _ in range(v-1):
        tmp = list(map(int,input().split()))
        tree_idx = tmp[0]
        tmp_idx = 1
        while True:
            if tmp[tmp_idx] == -1:
                break
            tree[tree_idx].append((tmp[tmp_idx],tmp[tmp_idx+1]))
            tmp_idx += 2
    return tree

def dfs(tree,visited,value,vx):
    visited[vx] = True
    ret_value = []
    for nx,nd in tree[vx]:
        if visited[nx] == True: continue
        ret_value.append(dfs(tree,visited,value+nd,nx))
    ret_value.sort(reverse=True)
    if ret_value == []:
        return value
    global answer
    if len(ret_value) >= 2:
        answer = max(answer,ret_value[0]+ret_value[1]-value*2)
    else:
        answer = max(answer,ret_value[0])
    return ret_value[0]

if __name__ == "__main__":
    main()