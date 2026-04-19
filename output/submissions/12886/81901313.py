from collections import deque

def main():
    print(solution(sorted(list(map(int,input().split())))))

def solution(start):
    start = convert(start)
    queue = deque([start])
    visited = {}
    visited[start] = 0
    move = [(2,1,0),(2,0,1),(1,0,2)]
    while queue:
        vx = queue.popleft()
        a,b,c = vx[0:4], vx[4:8], vx[8:12]
        if a == b and b == c: return 1
        va_vb_vc = [int(a),int(b),int(c)]
        for right, left, origin in move:
            nx = convert(sort_abc(va_vb_vc[right]-va_vb_vc[left],va_vb_vc[left]*2,va_vb_vc[origin]))
            if nx not in visited:
                visited[nx] = visited[vx] + 1
                queue.append(nx)
    return 0

def sort_abc(a,b,c):
    tmp = sorted([a,b,c])
    return tmp

def convert(abc):
    ret_value = ""
    for i in abc:
        if int(i) < 1000:
            ret_value += "0"
        if int(i) < 100:
            ret_value += "0"
        if int(i) < 10:
            ret_value += "0"
        ret_value += str(i)
    return ret_value

if __name__ == "__main__":
    main()