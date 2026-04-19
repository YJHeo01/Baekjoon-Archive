answer = 0

cube = list(map(int,input().split()))

high = []
low = []

if cube[0] == cube[1] == cube[2] == cube[3] and cube[8] == cube[9] == cube[10] == cube[11]:
    high = [[12,13],[4,5],[16,17],[20,21]]
    low = [[14,15],[6,7],[18,19],[22,23]]


if cube[4] == cube[5] == cube[6] == cube[7] and cube[20] == cube[21] == cube[22] == cube[23]:
    high = [[0,1],[17,19],[11,10],[14,12]]
    low = [[2,3],[16,18],[9,8],[15,13]]
    

if cube[12] == cube[13] == cube[14] == cube[15] and cube[16] == cube[17] == cube[18] == cube[19]:
    high = [[23,21],[0,2],[4,6],[8,10]]
    low = [[22,20],[1,3],[5,7],[9,11]]

if high == []:
    print(0)
    exit(0)

tmp = 1

for i in range(4):
    m = high[i] + low[(i+1)%4]
    value = cube[m[0]]
    for j in m:
        if value != cube[j]: tmp = 0

answer = max(answer,tmp)

tmp = 1

for i in range(4):
    m = high[i] + low[(i-1)%4]
    value = cube[m[0]]
    for j in m:
        if value != cube[j]: tmp = 0

answer = max(answer,tmp)

print(answer)