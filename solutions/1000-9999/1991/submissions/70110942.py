tree = [[]for _ in range(26)]

def preorder(idx):
    if chr(idx+65) == '.':
        return
    print(chr(65+idx),end="")
    preorder(tree[idx][0])
    preorder(tree[idx][1])
    return

def inorder(idx):
    if chr(idx+65) == '.':
        return
    inorder(tree[idx][0])
    print(chr(65+idx),end="")
    inorder(tree[idx][1])
    return

def postorder(idx):
    if chr(idx+65) == '.':
        return
    postorder(tree[idx][0])
    postorder(tree[idx][1])
    print(chr(65+idx),end="")
    return

n = int(input())

for _ in range(n):
    parent, left, right = input().split()
    parent, left, right = ord(parent)-65,ord(left)-65,ord(right)-65
    tree[parent]=[left,right]

preorder(0)
print()
inorder(0)
print()
postorder(0)
print()