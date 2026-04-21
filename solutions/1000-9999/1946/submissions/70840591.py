import sys

input = sys.stdin.readline

t = int(input())
INF = int(1e9)
for _ in range(t):
    n = int(input())
    applicant_list = []
    rank = [INF] * (n+1) #이 리스트를 활용하여 성적 중 하나가 다른 지원자보다 떨어지지 않는 지원자 구분
    for _ in range(n):
        a,b = map(int,input().split())
        applicant_list.append((a,b))
    applicant_list.sort()
    answer = 0
    for applicant in applicant_list:
        if rank[applicant[0]-1] > applicant[1]:
            answer += 1
        rank[applicant[0]] = min(rank[applicant[0]-1],applicant[1])
    print(answer)