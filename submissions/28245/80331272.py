import sys

input = sys.stdin.readline

def main():
    
    n = int(input())
    for _ in range(n):
        
        bitmask = get_bitmask(int(input()))

        if len(bitmask) == 1:
            value = bitmask.pop()
            if value == 0: print("0 0")
            else: print(value-1,value-1)
            continue
        
        need_plus_value = 2 ** bitmask[1]
        need_minus_value = 0
        
        while True:
            if len(bitmask) == 2: break
            value = bitmask.pop()
            need_minus_value += 2 ** value
            need_plus_value -= 2 ** value
        
        if need_plus_value < need_minus_value: bitmask[1] += 1
        
        print(bitmask.pop(),end=" ")
        print(bitmask.pop())

def get_bitmask(m):
    bitmask = []
    for i in range(60):
        if 2 ** i & m != 0:
            bitmask.append(i)
    bitmask.reverse()
    return bitmask

if __name__ == "__main__":
    main()