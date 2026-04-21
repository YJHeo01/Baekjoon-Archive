n = int(input())

arr = list(input().split())

first_exist = [False] * 26
second_exist = [False] * 26
possible = [False] * 26

for i in arr:
    for j in range(ord(i[0]) - ord('A')+1):
        if second_exist[j]:
            possible[ord(i[0]) - ord('A')] = True
            break
    for j in range(ord(i[1])-ord('A')+1):
        if first_exist[j]:
            possible[ord(i[1])-ord('A')] = True
            break
    for j in range(ord(i[0]) - ord('A'),26):
        if second_exist[j]:
            possible[j] = True
    for j in range(ord(i[1]) - ord('A'),26):
        if first_exist[j]:
            possible[j] = True
    first_exist[ord(i[0])-ord('A')] = True
    second_exist[ord(i[1])-ord('A')] = True

print(sum(possible))

for i in range(26):
    if possible[i] == False: continue
    print(chr(ord('A')+i),end=" ")