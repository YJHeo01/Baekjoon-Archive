def main():
    prime_list = prime()
    while True:
        print(solution(prime_list,input()))

def prime():
    prime_list = [True] * 100001
    ret_value = {}
    for i in range(2,100001):
        if prime_list[i] == True:
            ret_value[str(i)] = True
            for j in range(i+i,100001,i):
                prime_list[j] = False
    return ret_value
 
def solution(prime,s):
    if s == '0': exit(0)
    answer = 0
    s_length = len(s)
    for prime_length in range(5,0,-1):
        for end in range(prime_length,s_length+1):
            if s[end-prime_length:end] in prime:
                answer = max(answer,int(s[end-prime_length:end]))
        if answer != 0:
            break
    return answer

if __name__ == "__main__":
    main()