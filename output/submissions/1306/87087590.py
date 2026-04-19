import math

def main():
    n,m = map(int,input().split())
    s_length = 2 ** math.ceil(math.log2(n)+1)
    s = [-1] * (s_length)
    a = list(map(int,input().split()))
    leaf_start = s_length // 2 -1
    for i in range(n):
        s[leaf_start + i] = a[i]
    init(s,s_length-1)
    for i in range(m-1,n-m+1):
        print(query(s,i-(m-1)+leaf_start,i+(m-1)+leaf_start),end=" ")

def init(s,i):
    while True:
        if i == 1: break
        s[i//2] = max(s[i],s[i//2])
        i -= 1

def query(s,start,end):
    ret_value = -1
    while start <= end:
        if start % 2 == 1:
            ret_value = max(s[start],ret_value)
            start += 1
        if end % 2 == 0:
            ret_value = max(s[end],ret_value)
            end -= 1
        start = start // 2
        end = end // 2
    return ret_value

if __name__ == "__main__":
    main()