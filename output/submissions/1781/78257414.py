import sys

input = sys.stdin.readline

def main():
    n = int(input())
    homework = get_homework(n)
    answer = get_answer(homework,n)
    print(answer)

def get_homework(n):
    homework = []
    for _ in range(n):
        homework.append(list(map(int,input().split())))
    homework.sort(key= lambda x : -x[1])
    return homework

def get_answer(homework,n):
    answer = 0
    parent = get_init_parent(n)
    for deadline, ramen in homework:
        parent_node = find_parent(parent,deadline)
        if parent_node == 0: continue
        answer += ramen
        parent[parent_node] = parent_node - 1
    return answer

def get_init_parent(n):
    parent = [0] * (n+1)
    for i in range(1,n+1):
        parent[i] = i
    return parent

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main()