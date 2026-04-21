def backtracking(test_case,answer_list):
    if len(answer_list) == 6:
        for i in answer_list:
            print(i,end=" ")
        print()
        return
    for i in test_case:
        if answer_list != [] and i <= answer_list[-1]:
            continue
        backtracking(test_case,answer_list+[i])
    return


while 1:
    test_case = list(map(int,input().split()))
    if test_case[0] == 0:
        break
    backtracking(test_case[1:],[])