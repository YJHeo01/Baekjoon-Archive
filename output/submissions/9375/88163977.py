t = int(input())
for _ in range(t):
    n = int(input())
    cloth = dict([])
    data = []
    for _ in range(n):
        name, idx = input().split()
        if idx in cloth:
            cloth[idx].append(name)
        else:
            cloth[idx] = [name]
            data.append(idx)
    cnt = len(data)
    answer = 1
    for idx in cloth:
        answer *= (len(cloth[idx])+1)
    answer -= 1
    print(answer)