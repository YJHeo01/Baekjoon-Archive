import heapq

def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    q = []
    for i in range(n-1): heapq.heappush(q,(-matrix[i][1],i,i+1))
    answer = 0
    parent = [0] * n
    for i in range(1,n): parent[i] = i
    while q:
        mid, left_idx, right_idx = heapq.heappop(q)
        mid *= -1
        if matrix[left_idx][1] != mid: continue
        if union_parent(parent,left_idx,right_idx) == True:
            answer += (matrix[left_idx][0]*mid*matrix[right_idx][1])
            matrix[left_idx][1] = matrix[right_idx][1]
            matrix[right_idx][0] = matrix[left_idx][0]
            if left_idx != 0:
                heapq.heappush(q,(-matrix[left_idx][0],left_idx-1,left_idx))
            if right_idx + 1 < n:
                heapq.heappush(q,(-matrix[right_idx][1],right_idx,right_idx+1))
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