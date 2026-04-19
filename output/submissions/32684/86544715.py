multiple = [13,7,5,3,3,2]

c = list(map(int,input().split()))
e = list(map(int,input().split()))

c_score = 0
e_score = 1

for i in range(6):
    c_score += c[i] * multiple[i]
    e_score += e[i] * multiple[i]

if e_score >= c_score:
    print("ekwoo")
else:
    print("cocjr0208")