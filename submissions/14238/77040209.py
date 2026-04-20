data = list(input())

a,b,c = 0,0,0

for i in data:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    else:
        c += 1

def dfs(a,b,c,sentence):
    length = len(sentence)
    if a == 0 and b == 0 and c == 0:
        for i in sentence:
            print(i,end="")
        return True
    elif sentence == []:
        if a != 0 and dfs(a-1,b,c,['A']) == True:
            return True
        if b != 0 and dfs(a,b-1,c,['B']) == True:
            return True
        if c != 0 and dfs(a,b,c-1,['C']) == True:
            return True
    elif sentence[-1] == 'A':
        if a != 0 and dfs(a-1,b,c,sentence+['A']) == True:
            return True
        if b != 0 and dfs(a,b-1,c,sentence+['B']) == True:
            return True
        if c != 0:
            if length == 1 or sentence[-2] != 'C':
                if dfs(a,b,c-1,sentence+['C']) == True:
                    return True
    elif sentence[-1] == 'B':
        if a != 0 and dfs(a-1,b,c,sentence+['A']) == True:
                return True
        if c != 0:
            if length == 1 or sentence[-2] != 'C':
                if dfs(a,b,c-1,sentence+['C']) == True:
                    return True
    else:
        if a != 0 and dfs(a-1,b,c,sentence+['A']) == True:
                return True
        if b != 0 and dfs(a,b-1,c,sentence+['B']) == True:
            return True
    return False

search_correct_record = dfs(a,b,c,[])

if search_correct_record == False:
    print(-1)