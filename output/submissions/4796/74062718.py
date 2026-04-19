case_idx = 1

while True:
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break
    answer = (v//p) * l + v % p
    print("Case " + str(case_idx) + ": " + str(answer))
    case_idx += 1