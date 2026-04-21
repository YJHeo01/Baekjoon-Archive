n,k = map(int,input().split())
array = [0] + sorted(list(map(int,input().split())))
distance_list = []
for i in range(n):
    distance_list.append(array[i+1] - array[i])
distance_list.sort()
print(sum(distance_list[:k]))