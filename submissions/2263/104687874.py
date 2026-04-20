import sys

sys.setrecursionlimit(100010)

n = int(input())

inOrder = list(map(int,input().split()))
postOrder = list(map(int,input().split()))

inOrder_pos = [-1] * (n+1)
postOrder_pos = [-1] * (n+1)

for i in range(n):
    inOrder_pos[inOrder[i]] = i
    postOrder_pos[postOrder[i]] = i

def func(i_l,i_r,p_l,p_r):
    if i_l > i_r or p_l > p_r: return
    print(postOrder[p_r],end=" ")
    root = inOrder_pos[postOrder[p_r]]
    left_size = root - i_l
    right_size = i_r - root
    func(i_l,root-1,p_l,p_l+left_size-1)
    func(root+1,i_r,p_r-right_size,p_r-1)

func(0,n-1,0,n-1)