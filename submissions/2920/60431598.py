data = list(map(int,input().split()))

if data[0] + 1 == data[1] :
    for i in range(0,7):
        if data[i] + 1 != data[i+1]:
            print("mixed")
            break
    print("ascending")
elif data[0] == data[1] + 1 :
    for i in range(0,7):
        if data[i] - 1 != data[i+1]:
            print("mixed")
            break
    print("descending")
else : print("mixed")