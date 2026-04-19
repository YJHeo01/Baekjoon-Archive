n = int(input())
file = list(map(int,input().split()))
cluster_size = int(input())
cnt = 0
for file_size in file:
    cnt += file_size // cluster_size
    if file_size % cluster_size != 0: cnt += 1
print(cluster_size*cnt)