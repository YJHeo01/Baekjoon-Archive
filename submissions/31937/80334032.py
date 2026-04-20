import sys

input = sys.stdin.readline

def main():
    
    n,m,k = map(int,input().split())
    
    possible_answer = [False] * (n+1)
    virus = [False] * (n+1)
    for i in list(map(int,input().split())):
        virus[i] = True
        possible_answer[i] = True
    
    system_log = []
    for _ in range(m):
        system_log.append(list(map(int,input().split())))
    system_log.sort()

    for t,a,b in system_log:
        if virus[b] == False: possible_answer[a] = False
        if virus[a] == False or possible_answer[a] == False: continue
        print(a)
        break

if __name__ == "__main__":
    main()