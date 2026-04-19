import heapq

def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    q = []
    for i in range(n-1): heapq.heappush(q,(matrix[i][0] * matrix[i][1] * matrix[i+1][1],i,i+1))
    answer = 0
    parent = [0] * n
    for i in range(1,n): parent[i] = i
    while q:
        value , l_idx, r_idx = heapq.heappop(q)
        if matrix[l_idx][0] * matrix[l_idx][1] * matrix[r_idx][1] != value: continue
        if union_parent(parent,l_idx,r_idx) == True:
            answer += value
            matrix[l_idx][1] = matrix[r_idx][1]
            matrix[r_idx][0] = matrix[l_idx][0]
            if l_idx != 0:
                heapq.heappush(q,(matrix[l_idx-1][1]*matrix[l_idx][0]*matrix[l_idx][1],l_idx-1,l_idx))
            if r_idx + 1 < n:
                heapq.heappush(q,(matrix[r_idx][0]*matrix[r_idx][1]*matrix[r_idx+1][1],r_idx,r_idx+1))
    print(answer)

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    elif b > a:
        parent[a] = b
    else:
        return False
    return True

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

if __name__ == "__main__":
    main() 