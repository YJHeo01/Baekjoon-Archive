num_list = [[] for _ in range(51)]

n = int(input())
max_i = 0
for _ in range(n):
    tmp = list(input())
    tmp.reverse()
    l = len(tmp)
    for i in range(l):
        if ord(tmp[i]) < ord('A'):
            num = int(tmp[i])
        else:
            num = 10 + ord(tmp[i]) - ord('A') #36진수 -> 10진수
        num_list[i].append(num)
    max_i = max(l-1,max_i)
change_list = []
k = int(input())
for i in range(max_i):
    num_list[i].sort()
tmp = 0
for i in range(max_i,-1,-1): 
    for j in num_list[i]:
        if j in change_list or k <= 0 or j == 35 :
            continue
        change_list.append(j)
        k -= 1

l = 0

for i in range(max_i,-1,-1):
    for j in num_list[i]:
        if j in change_list:
            tmp += 35 * (36 ** i)
        else:
            tmp += j * (36 ** i)

while 1:
    a = tmp // (36 ** l)
    if a == 0:
        break
    l += 1
answer = []
if tmp == 0 :
    answer.append('0')
for i in range(l-1,-1,-1):
    a = tmp // (36 ** i)
    if a >= 10:
        t = chr(a - 10 + ord('A'))
    else:
        t = str(a)
    answer.append(t)
    tmp -= (a * (36 ** i))
for c in answer:
    print(c,end="")