answer = 0

s = list(input())
t = list(input())

t_a_cnt, t_b_cnt = 0,0
s_a_cnt, s_b_cnt = 0,0
l = len(t)
for i in t:
    if i == 'A':
        t_a_cnt += 1
    else:
        t_b_cnt += 1

for i in s:
    if i == 'A':
        s_a_cnt += 1
    else:
        s_b_cnt += 1

def game(string,a_cnt,b_cnt):
    global answer
    if string == t:
        answer = 1
        return
    if a_cnt < t_a_cnt:
        game(string+['A'],a_cnt+1,b_cnt)
    if b_cnt < t_b_cnt:
        tmp = string+['B']
        tmp.reverse()
        game(tmp,a_cnt,b_cnt+1)
    return

game(s,s_a_cnt,s_b_cnt)

print(answer)