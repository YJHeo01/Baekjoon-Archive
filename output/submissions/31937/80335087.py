import sys

input = sys.stdin.readline

def main():
    
    n,m,k = map(int,input().split())
    
    first_transfer_time = [int(1e9)+1] * (n+1)
    possible_answer = [False] * (n+1)
    virus = [False] * (n+1)
    
    if k == 1:
        print(input()) #바이러스가 하나일 경우 더 확인해 볼 필요 없음
        return
    
    for i in list(map(int,input().split())): #둘째 줄 입력, 감염된 컴퓨터의 목록
        virus[i] = True
        possible_answer[i] = True #바이러스 인 경우 정답이 될 수도 있음

    system_log = []
    for _ in range(m):
        t,a,b = map(int,input().split())
        if virus[b] == False:
            possible_answer[a] = False #b가 virus가 아닌 경우, a는 virus의 근원지가 될 수 없음
        if first_transfer_time[a] > t:
            first_transfer_time[a] = t
        system_log.append([t,a,b])

    system_log.sort()
    answer = 0

    for i in range(1,n+1):
        if possible_answer[i] == True:
            if first_transfer_time[i] < first_transfer_time[answer]:
                answer = i
    
    print(answer)

if __name__ == "__main__":
    main()