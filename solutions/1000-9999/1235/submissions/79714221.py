import sys

input = sys.stdin.readline

def main():
    n = int(input())
    student = []
    for _ in range(n):
        student.append(list(input()))
    length = len(student)
    answer = n
    for k in range(1,n):
        complete = True
        visited = [False] * (10**k)
        for i in range(n):
            idx = int(''.join(student[i][n-k:n]))
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