a,b = map(int,input().split())

answer = []

cnt = 0
while True:
    if a == 0 or b == 0 or b >= a:
        print("NO")
        exit(0)
    cnt += 1
    if a == b + 1:
        tmp = ''
        for _ in range(b):
            tmp += 'ab'
        tmp += 'a'
        answer.append(tmp)
        break

    a -= 2; b -= 1
    answer.append("aba")
print("YES")
print(cnt)

for s in answer:
    print(s)
