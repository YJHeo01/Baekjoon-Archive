q = int(input())

for _ in range(q):
    a,b = map(int,input().split())
    inner_distance = 0
    outer_distance = 0
    tmp_a, tmp_b = a,b
    while True:
        if tmp_a == tmp_b: break
        inner_distance += 1
        tmp_a += 1
        if tmp_a >= 244: tmp_a = 201
    tmp_a, tmp_b = a,b
    while True:
        if tmp_a == tmp_b: break
        outer_distance += 1
        tmp_a -= 1
        if tmp_a <= 200: tmp_a = 243
    if inner_distance < outer_distance:
        print("Inner circle line")
    elif inner_distance > outer_distance:
        print("Outer circle line")
    else:
        print("Same")