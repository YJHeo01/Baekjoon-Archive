import sys

input = sys.stdin.readline

def main():
    n = int(input())
    student = []
    for _ in range(n):
        student.append(list(input().rstrip()))
    length = len(student)
    answer = length
    for k in range(1,length):
        complete = True
        visited = [False] * (10**k)
        for i in range(n):
            idx = int(''.join(student[i][length-k:length]))
            if visited[idx] == True:
                complete = False
                break
            else:
                visited[idx] = True
        if complete == True:
            answer = k
            break
    print(answer)

if __name__  == "__main__":
    main()