n,c = map(int,input().split())

weight = list(map(int,input().split()))
bag = dict()
bag[0] = 1

for i in weight:
    new_bag = dict()
    for j in bag:
        if i + j <= c:
            new_value = i + j
            if new_value in new_bag:
                new_bag[new_value] += bag[j]
            else:
                new_bag[new_value] = bag[j]
    for new_value in new_bag:
        if new_value in bag:
            bag[new_value] += new_bag[new_value]
        else:
            bag[new_value] = new_bag[new_value]

answer = 0

for i in bag:
    answer += bag[i]

print(answer)