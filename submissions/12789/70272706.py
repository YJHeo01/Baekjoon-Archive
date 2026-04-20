n = int(input())

student_list = list(map(int,input().split()))

void_space = []

result = []

for i in range(n-1):
    if student_list[i+1] < student_list[i]:
        void_space.append(student_list[i])
    else:
        while 1:
            if void_space == []:
                void_space.append(student_list[i])
                break
            if void_space[-1] < student_list[i]:
                result.append(void_space.pop())
            else:
                result.append(student_list[i])
                break

result.append(student_list[-1])

void_space.reverse()

result = result + void_space

answer = "Nice"

for i in range(n):
    if result[i] != i + 1:
        answer = "Sad"
        break
print(answer) 