s = list(input())
length = len(s)
a,b,c = 0,0,0
for i in s:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    else:
        c += 1

def solution_A(a,b,c):
    answer = [0] * length
    c -= 1
    answer[0] = 'C'
    if length <= 1:
        return answer
    if b != 0:
        b -= 1
        answer[1] = 'B'
    elif a != 0:
        a -= 1
        answer[1] = 'A'
    else:
        answer[0] = -1
        return answer
    for i in range(2,length):
        if answer[i-2] == 'C':
            if answer[i-1] == 'B':
                if a != 0:
                    answer[i] = 'A'
                    a -= 1
                else:
                    answer[0] = -1
                    return answer
            else:
                if b != 0:
                    b -= 1
                    answer[i] = 'B'
                elif a != 0:
                    a -= 1
                    answer[i] = 'A'
                else:
                    answer[0] = -1
                    return answer
        elif answer[i-1] == 'C':
            if b != 0:
                b -= 1
                answer[i] = 'B'
            elif a != 0:
                a -= 1
                answer[i] = 'A'
            else:
                answer[0] = -1
                return answer
        else:
            if c != 0:
                c -= 1
                answer[i] = 'C'
            elif answer[i-1] == 'B':
                if a != 0:
                    a -= 1
                    answer[i] = 'A'
                else:
                    answer[0] = -1
                    return answer
            else:
                if b != 0:
                    b -= 1
                    answer[i] = 'B'
                else:
                    a -= 1
                    answer[i] = 'A'
    return answer

def solution_B(a,b,c):
    answer = [0] * length
    b -= 1
    answer[0] = 'B'
    if length <= 1:
        return answer
    if c != 0:
        c -= 1
        answer[1] = 'C'
    elif a != 0:
        a -= 1
        answer[1] = 'A'
    else:
        answer[0] = -1
        return answer
    for i in range(2,length):
        if answer[i-2] == 'C':
            if answer[i-1] == 'B':
                if a != 0:
                    answer[i] = 'A'
                    a -= 1
                else:
                    answer[0] = -1
                    return answer
            else:
                if b != 0:
                    b -= 1
                    answer[i] = 'B'
                elif a != 0:
                    a -= 1
                    answer[i] = 'A'
                else:
                    answer[0] = -1
                    return answer
        elif answer[i-1] == 'C':
            if b != 0:
                b -= 1
                answer[i] = 'B'
            elif a != 0:
                a -= 1
                answer[i] = 'A'
            else:
                answer[0] = -1
                return answer
        else:
            if c != 0:
                c -= 1
                answer[i] = 'C'
            elif answer[i-1] == 'B':
                if a != 0:
                    a -= 1
                    answer[i] = 'A'
                else:
                    answer[0] = -1
                    return answer
            else:
                if b != 0:
                    b -= 1
                    answer[i] = 'B'
                else:
                    a -= 1
                    answer[i] = 'A'
    return answer
answer_A = [-1]
answer_B = [-1]
all_A = True
if c != 0:
    answer_A = solution_A(a,b,c)
    all_A = False
if b != 0:
    answer_B = solution_B(a,b,c)
    all_A = False

if all_A == True:
    for i in s:
        print(i,end="")
elif answer_A[0] != -1:
    for i in answer_A:
        print(i,end="")
elif answer_B[0] != -1:
    for i in answer_B:
        print(i,end="")
else:
    print(-1)