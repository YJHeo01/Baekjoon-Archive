data = list(map(int,input().split()))

index = 0
if data[0] + 1 == data[1] :
    index = 1
    for i in range(0,7):
        if data[i] + 1 != data[i+1]:
            index = 0
            break
elif data[0] == data[1] + 1 :
    index = 2
    for i in range(0,7):
        if data[i] - 1 != data[i+1]:
            index = 0
            break

if index == 0: print("mixed")
elif index == 1 : print("ascending")
else : print("descending")
        