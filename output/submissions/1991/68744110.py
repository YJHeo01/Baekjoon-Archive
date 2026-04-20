n = int(input())
MAX_V = 7000

def preorder(tree,i):
    print(tree[i],end='')
    if 2*i<MAX_V and tree[2*i] != 0:
        preorder(tree,2*i)
    if 2*i+1<MAX_V and tree[2*i+1] != 0:
        preorder(tree,2*i+1)

def inorder(tree,i):
    if 2*i<MAX_V and tree[2*i] != 0:
        inorder(tree,2*i)
    print(tree[i],end='')
    if 2*i+1<MAX_V and tree[2*i+1] != 0:
        inorder(tree,2*i+1)

def postorder(tree,i):
    if 2*i<MAX_V and tree[2*i] != 0:
        postorder(tree,2*i)
    if 2*i+1<MAX_V and tree[2*i+1] != 0:
        postorder(tree,2*i+1)
    print(tree[i],end='')

def node_insert(tree,b,c,i):
    if b != '.':
        tree[2*i] = b
    if c != '.':
        tree[2*i+1] = c
    return

def node_search(tree,a,b,c,i):
    if tree[1] == 0:
        tree[1] = a
        node_insert(tree,b,c,i)
        return
    if tree[i] == a:
        node_insert(tree,b,c,i)
        return
    else:
        next = 2*i
        if next <= MAX_V:
            if tree[next] != 0:
                node_search(tree,a,b,c,next)
            if tree[next+1] != 0:
                node_search(tree,a,b,c,next+1)
        return

tree = [0] * MAX_V
for i in range(n):
    a,b,c = input().split()
    if b == '.' and c == '.':
        continue
    node_search(tree,a,b,c,1)

preorder(tree,1)
print()
inorder(tree,1)
print()
postorder(tree,1)
