#https://www.acmicpc.net/board/view/145640 체크용 제출
s = int(input())
  
sum_value = 0
cnt = 0
for cnt in range(1, s + 1):
    sum_value += cnt
    if sum_value > s:
        break

print(cnt - 1)