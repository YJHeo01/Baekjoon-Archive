n = int(input())

word_list = []

for _ in range(n):
    tmp = input()
    length = len(tmp)
    word_list.append((length,tmp))

word_list.sort(reverse=True)

answer = 0

word_set = []

for new_length, new_c in word_list:
    check = True
    for cur_length, cur_c in word_set:
        if new_c != cur_c[:new_length]:
            continue
        check = False
        break
    if check == True:
        answer += 1
        word_set.append((new_length,new_c))

print(answer)