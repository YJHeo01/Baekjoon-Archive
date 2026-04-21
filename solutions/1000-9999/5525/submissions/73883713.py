n = int(input())
m = int(input())

array = list(input())

def check_O(array,idx):
    if array[idx] == 'O':
        return True
    else:
        return False
    
def check_I(array,idx):
    if array[idx] == 'I':
        return True
    else:
        return False
    
def check_IOIOI(array,idx):
    for _ in range(n):
        idx += 1
        if check_O(array,idx) == False:
            return False
        idx += 1
        if check_I(array,idx) == False:
            return False
    return True

answer = 0

for i in range(m-(2*n)):
    if array[i] == 'I' and check_IOIOI(array,i):
        answer += 1
    
print(answer)
