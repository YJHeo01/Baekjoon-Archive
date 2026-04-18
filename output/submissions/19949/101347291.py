from itertools import product

a = list(map(int,input().split()))

test_case_list = list(product(list(range(1,6)),repeat=10))

answer = 0

for test_case in test_case_list:
    bibup = True
    for i in range(1,8):
        if test_case[i] == test_case[i-1] and test_case[i] == test_case[i+1]:
            bibup = False
    if bibup == False: continue
    score = 0
    for i in range(10):
        if test_case[i] == a[i]: score += 1
    if score >= 5: answer += 1

print(answer)