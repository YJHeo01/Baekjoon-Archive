t = int(input())

sieve = [True] * 10001

prime = []

for i in range(2,10001):
    if sieve[i]:
        prime.append(i)
        for j in range(i+i,10001,i):
            sieve[j] = False

def solution(idx):
    print(f"Scenario #{idx}:")
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    for i in range(1,n):
        arr[i] //= arr[0]
    arr[0] = 1
    l = int(input())
    for _ in range(l):
        a,b = map(int,input().split())
        left, right = a,b
        for p in prime:
            if left < p and right < p: break
            if left == 1 or right == 1: break
            if left % p == 0 and right % p == 0:
                while True:
                    if left % p != 0 or right % p != 0: break
                    if left == 1 or right == 1: break
                    left //= p; right //= p
        for i in arr[1:]:
            while True:
                if left % i != 0 or left == 1: break
                left //= i
        for i in arr[1:]:
            while True:
                if right % i != 0 or right == 1: break
                right //= i
        if left == 1 and right == 1:
            print(f"Gear ratio {a}:{b} can be realized.")
        else:
            print(f"Gear ratio {a}:{b} cannot be realized.")
    print()
    
    
for i in range(t):
    solution(i+1)