n,m = map(int,input().split())

num_list = set()

def f(num_list,cur_value,target_value):
    if cur_value == target_value:
        print("YES")
        exit(0)
    if cur_value < target_value:
        return
    if cur_value // 2 not in num_list:
        num_list.add(cur_value//2)
        f(num_list,cur_value//2,target_value)
    if cur_value % 2 == 1 and cur_value // 2 + 1 not in num_list:
        num_list.add(cur_value//2+1)
        f(num_list,cur_value//2+1,target_value)

f(num_list,n,m)

print("NO")