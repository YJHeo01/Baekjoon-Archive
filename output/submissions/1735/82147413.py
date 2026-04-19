a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())

def Euclidean(a,b):
    if b == 0:
        return a
    return Euclidean(b,a%b)

b_answer = b1 * b2 // Euclidean(max(b1,b2),min(b1,b2))
a_answer = a1 * b_answer // b1 + a2 * b_answer // b2

tmp = Euclidean(max(a_answer,b_answer),min(a_answer,b_answer))

a_answer = a_answer // tmp; b_answer = b_answer // tmp

print(a_answer,b_answer)