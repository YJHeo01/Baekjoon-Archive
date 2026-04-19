import sys

input = sys.stdin.readline

def main():
    n = int(input())
    student = []
    for _ in range(n):
        student.append(input().rstrip())
    length = len(student[0])
    answer = length
    for i in range(1,length):
        finish = True
        tmp = {}
        for s in student:
            if s[length-i:] in tmp:
                finish = False
                break
            tmp[s[length-i:]] = True
        if finish == True:
            answer = i
            break
    print(answer)

if __name__ == "__main__":
    main()