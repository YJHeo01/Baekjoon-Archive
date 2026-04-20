import sys

input = sys.stdin.readline

answer_list = [1] * 1000000
def find_parent(parent,x):
    if parent[x] == -1:
        parent[x] = x
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_set(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
        answer_list[a] += answer_list[b]
        return a
    elif a>b:
        parent[a] = b
        answer_list[b] += answer_list[a]
        return b
    else:
        return a
t = int(input())

name_list = []
parent = [-1] * 1000000


for _ in range(t):
    f = int(input())    
    for i in range(f):
        a,b = input().split()
        a = list(a)
        b = list(b)
        h_a = 0
        h_1 = 1
        h_2 = 1
        h_b = 0
        l = len(a)
        for i in range(l):
            tmp = ord(a[i]) - ord('A') +1 
            if i % 2 == 0:
                h_1 += tmp
                h_2 *= tmp
            else:
                h_1 *= tmp
                h_2 += tmp
        h_a = h_1+h_2*10
        h_a %= 1000000
        h_1,h_2 = 1,1
        l = len(b)
        for i in range(l):
            tmp = ord(b[i]) - ord('A')+1
            if i % 2 == 0:
                h_1 += tmp
                h_2 *= tmp
            else:
                h_1 *= tmp
                h_2 += tmp
        h_b = h_1 + h_2*10
        h_b %= 1000000
        answer = union_set(parent,h_a,h_b)
        print(answer_list[answer])
    parent = [-1] * 1000000
    answer_list = [1] * 1000000