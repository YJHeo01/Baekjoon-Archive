import sys, math

input = sys.stdin.readline

def main():
    print('<',end="")
    for i in range(n):
        init(i)
    cur_idx = 0
    for i in range(n):
        target = k
        if i != 0: print(', ',end="")
        tmp = query(cur_idx,n-1)
        if tmp < target:
            target -= tmp
            cur_idx = 0
        target %= (n-i)
        if target == 0: target = n - i
        left, right = cur_idx, n-1
        answer = -1
        while left <= right:
            mid = (left+right) // 2
            tmp = query(cur_idx,mid)
            if tmp >= target:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        print(answer+1,end="")
        update(answer)
        cur_idx = answer
    print('>')

def init(i):
    i += tree_size
    tree[i] += 1
    i //= 2
    while i:
        tree[i] = tree[2*i] + tree[2*i+1]
        i //= 2

def update(i):
    i += tree_size
    tree[i] -= 1
    i //= 2
    while i:
        tree[i] = tree[2*i] + tree[2*i+1]
        i //= 2

def query(l, r):
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

if __name__ == "__main__":
    n,k = map(int,input().split())
    tree_size = 2 ** math.ceil(math.log2(n))
    tree = [0] * (2 * tree_size)
    main()