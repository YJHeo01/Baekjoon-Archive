import sys, math

input = sys.stdin.readline

n,q = map(int,input().split())

x_list = list(map(int,input().split()))

y_list = list(map(int,input().split()))

prefix_sum_LtoR = [0] * (n+1)
prefix_sum_RtoL = [0] * (n+1)

for i in range(1,n):
    x_l, y_l = x_list[i-1], y_list[i-1]
    x_r, y_r = x_list[i], y_list[i]
    dist = math.sqrt((x_l-x_r) ** 2 + (y_l-y_r) ** 2)
    prefix_sum_LtoR[i+1] = prefix_sum_LtoR[i] + dist
    prefix_sum_RtoL[i+1] = prefix_sum_RtoL[i] + dist
    if y_l <= y_r: prefix_sum_LtoR[i+1] += dist
    else: prefix_sum_RtoL[i+1] += dist
    if y_l < y_r: prefix_sum_LtoR[i+1] += dist
    else: prefix_sum_RtoL[i+1] += dist

for _ in range(q):
    l,r = map(int,input().split())
    if l >= r: print(prefix_sum_RtoL[l]-prefix_sum_RtoL[r])
    else: print(prefix_sum_LtoR[r]-prefix_sum_LtoR[l])