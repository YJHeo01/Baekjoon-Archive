from collections import deque

def main():
    n = int(input())
    prime = get_prime(n)
    queue = deque([])
    b,s = 0,0
    check_reverse = False
    for i in range(1,n+1):
        if prime[i] == False:
            if check_reverse == False:
                queue.append('B')
            else:
                queue.appendleft('B')
            b += 1
        else:
            if check_reverse == False:
                value = queue.pop()
                queue.appendleft('S')
                queue.appendleft('S')
            else:
                value = queue.popleft()
                queue.append('S')
                queue.append('S')
            if value == 'B':
                b -=1; s += 1
            check_reverse = ~check_reverse
            
            s += 1
    print(b,s)

def get_prime(n):
    prime = [True] * (n+1)
    prime[1] = False
    for i in range(2,n+1):
        if prime[i] == True:
            value = i + i
            while True:
                if value > n: break
                prime[value] = False
                value += i
    return prime

if __name__ == "__main__":
    main()