import sys

input = sys.stdin.readline

def main():
    n = int(input())
    prime = [True] * (n+1)
    for i in range(2,n+1):
        if prime[i]:
            if sosusangkeun(i): print(i)
            for j in range(i,n+1,i):
                prime[j] = False


def sosusangkeun(value):
    visited = [False] * (1001)
    cur_value = value
    while True:
        new_value = get_new_value(cur_value)
        if new_value == 1: return True
        if visited[new_value]: return False
        visited[new_value] = True
        cur_value = new_value
        
def get_new_value(value):
    ret_value = 0
    while True:
        if value == 0:
            break
        tmp = value % 10
        ret_value += tmp ** 2
        value = value // 10
    return ret_value

if __name__ == "__main__":
    main()