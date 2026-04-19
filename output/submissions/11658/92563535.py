import sys, math

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

tree_size = 1 << math.ceil(math.log2(n))

tree = [[0]*(tree_size*2) for _ in range(n)]

def init(tree,row):
    for i in range(n):
        tree[tree_size+i] = arr[row][i]
    i = tree_size - 1
    while True:
        if i == 0: break
        tree[i] = tree[i*2] + tree[i*2+1]
        i -= 1
    
for i in range(n):
    init(tree[i],i)

def update(tree,i,value):
    i += tree_size
    tree[i] = value
    i //= 2
    while i:
        tree[i] = tree[2*i] + tree[2*i+1]
        i //= 2

def query(tree,l, r):
    l += tree_size
    r += tree_size
    ret_value = 0
    while l <= r:
        if l % 2 == 1:
            ret_value += tree[l]
            l += 1
        if r % 2 == 0:
            ret_value += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return ret_value

answer = ''

for _ in range(m):
    w, *tmp = input().split()
    if w == '0':
        x,y,c = map(int,tmp)
        x -= 1; y -= 1
        update(tree[x],y,c)
    else:
        x1,y1,x2,y2 = map(int,tmp)
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        tmp = 0
        for i in range(x1,x2+1):
            tmp += query(tree[i],y1,y2)
        answer += str(tmp)
        answer += '\n'
        
sys.stdout.write(answer)