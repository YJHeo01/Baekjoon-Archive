answer = [0,0,0]

def paper(start_x,end_x,start_y,end_y,array):
    v = array[start_x][start_y]
    if start_x + 1 == end_x:
        answer[v] += 1
        return
    for i in range(start_x,end_x):
        for j in range(start_y,end_y):
            if v != array[i][j]:
                n = (end_x - start_x) // 3
                paper(start_x,start_x+n,start_y,start_y+n,array)
                paper(start_x,start_x+n,start_y+n,end_y-n,array)
                paper(start_x,start_x+n,end_y-n,end_y,array)
                paper(start_x+n,end_x-n,start_y,start_y+n,array)
                paper(start_x+n,end_x-n,start_y+n,end_y-n,array)
                paper(start_x+n,end_x-n,end_y-n,end_y,array)
                paper(end_x-n,end_x,start_y,start_y+n,array)
                paper(end_x-n,end_x,start_y+n,end_y-n,array)
                paper(end_x-n,end_x,end_y-n,end_y,array)
                return
    answer[v] += 1
            


n = int(input())
array = []
for i in range(n):
    tmp = list(map(int,input().split()))
    array.append(tmp)
paper(0,n,0,n,array)
print(answer[2])
print(answer[0])
print(answer[1])