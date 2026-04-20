import sys

input = sys.stdin.readline

def main():
    jump = [list(map(int,input().split())) for _ in range(n)]
    jump.sort()
    distance = [INF] * n
    answer = solution(jump,distance)
    if answer >= INF:
        print("Ducks can't fly")
    else:
        print(answer)

def solution(jump,distance):
    ret_value = INF
    for i in range(n):
        if jump[i][0] >= s: break
        if jump[i][0] == 0: distance[i] = 0
        if distance[i] + s - jump[i][0] >= ret_value: continue
        if distance[i] + jump[i][1] >= s:
            ret_value = min(ret_value,s-jump[i][0]+jump[i][1])
            continue
        for j in range(i+1,n):
            if jump[j][0] > jump[i][0] + jump[i][1]: break
            distance[j] = min(distance[j],jump[i][0]+jump[i][1]-jump[j][0]+distance[i])
    return ret_value

if __name__ == "__main__":
    INF = int(1e15)
    n,s = map(int,input().split())
    main()