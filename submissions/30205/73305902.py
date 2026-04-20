import sys

input = sys.stdin.readline

n,m,p = map(int,input().split())

def solution(power):
    for _ in range(n):
        item_cnt = 0
        building = list(map(int,input().split()))
        building.sort()
        for floor in building:
            if floor == -1:
                item_cnt += 1
                continue
            if power >= floor:
                power += floor
            else:
                for i in range(item_cnt):
                    power *= 2
                    if power >= floor:
                        power *= 2
                        item_cnt -= (i+1)
                        break
                if power < floor:
                    return 0
        power *= (2**item_cnt)
    return 1


print(solution(p))