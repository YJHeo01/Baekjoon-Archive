a = list(map(int,input().split()))

answer = 0

def backtracking(submission,length):
    if length == 10:
        score = 0
        for i in range(10):
            if a[i] == submission[i]:
                score += 1
        if score >= 5: return 1
        else: return 0
    ret_value = 0
    for i in range(1,6):
        if i == submission[length-1] and submission[length-1] == submission[length-2]: continue
        submission.append(i)
        ret_value += backtracking(submission,length+1)
        submission.pop()
    return ret_value


for i in range(1,6):
    for j in range(1,6):
        answer += backtracking([i,j],2)

print(answer)