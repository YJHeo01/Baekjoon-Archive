def main():
    array = list(map(int,input().split()))
    answer = solution(array)
    print(answer)

def solution(array):
    visited = [False] * 14
    answer = set_k(array,visited,{})
    return answer

def set_k(array,visited,value):
    C,G = array[2], array[6]
    ret_value = 0
    for k in range(1,14):
        visited[k] = True; value['k'] = k
        ret_value += set_c_g(array,visited,value)
        visited[k] = False
    return ret_value

def set_c_g(array,visited,value):
    ret_value = 0
    sum_c_g = array[2] - value['k']
    for c in range(1,sum_c_g):
        g = sum_c_g - c
        if c > 13 or g > 13 or visited[c] or visited[g] or c == g: continue
        visited[c], visited[g] = True, True
        value['c'], value['g'] = c,g
        ret_value += set_i_j(array,visited,value)
        visited[c], visited[g] = False, False
    return ret_value

def set_i_j(array,visited,value):
    ret_value = 0
    sum_i_j = array[6] - value['k']
    for i in range(1,sum_i_j):
        j = sum_i_j - i
        if i > 13 or j > 13 or visited[i] or visited[j] or i == j: continue
        visited[i], visited[j] = True, True
        value['i'], value['j'] = i,j
        ret_value += set_d_h(array,visited,value)
        visited[i], visited[j] = False, False
    return ret_value

def set_d_h(array,visited,value):
    D = array[3]
    ret_value = 0
    for d in range(1,D):
        h = D - d
        if d > 13 or h > 13 or visited[d] or visited[h] or d == h: continue
        visited[d], visited[h] = True, True
        value['d'] = d; value['h'] = h
        ret_value += set_l_m(array,visited,value)
        visited[d], visited[h] = False, False
    return ret_value

def set_l_m(array,visited,value):
    H = array[7]
    ret_value = 0
    for l in range(1,H):
        m = H - l
        if m > 13 or l > 13 or visited[m] or visited[l] or m == l: continue
        visited[m], visited[l] = True, True
        value['m'], value['l'] = m,l
        ret_value += set_b_f(array,visited,value)
        visited[m], visited[l] = False, False
    return ret_value

def set_b_f(array,visited,value):
    ret_value = 0
    b_f_sum = array[1] - value['j'] - value['m']
    for b in range(1,b_f_sum):
        f = b_f_sum - b
        if b > 13 or f > 13 or visited[b] or visited[f] or b == f: continue
        visited[b], visited[f] = True, True
        value['b'], value['f'] = b,f
        ret_value += set_a_e(array,visited,value)
        visited[b], visited[f] = False, False
    return ret_value

def set_a_e(array,visited,value):
    ret_value = 0
    a_e_sum = array[0] - value['i'] - value['l']
    for a in range(1,a_e_sum):
        e = a_e_sum - a
        if a > 13 or e > 13 or visited[a] or visited[e] or a == e: continue
        if a + value['b'] + value['c'] + value['d'] == array[4] and array[5] == e + value['f'] + value['g'] + value['h']:
            return 1
    return 0

if __name__ == "__main__":
    main()