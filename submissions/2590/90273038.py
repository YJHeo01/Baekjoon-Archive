n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

answer = int(input())

answer += n5

n1 -= n5 * 11

answer += n4

n2 -= n4 * 5

answer += n3 // 4

n3_mod = n3 % 4

if n3_mod != 0:
    answer += 1
    
if n3_mod == 1:
    n2 -= 5
    n1 -= 7

if n3_mod == 2:
    n2 -= 3
    n1 -= 6
    
if n3_mod == 3:
    n2 -= 1
    n1 -= 5
    
    
if n2 <= 0:
    n1 += n2 * 4
else:
    answer += n2 // 9
    n2_mod = n2 % 9
    if n2_mod != 0: 
        answer += 1
        n1 -= (36-4*n2_mod) 
    
if n1 > 0: answer += n1

print(answer)