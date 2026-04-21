from itertools import combinations

t = int(input())

for _ in range(t):
    n,m,k = map(int,input().split())
    min_value = int(1e10)
    max_value = 0
    B = list(map(int,input().split()))
    A = list(map(int,input().split()))
    tmp_a = []
    tmp_b = list(combinations(range(n),k))
    tmp_a = list(combinations(range(m),k))
    bob = []
    alice = []
    for test_case in tmp_b:
        tmp = 0
        for i in test_case:
            tmp += B[i]
        bob.append(tmp)
    for test_case in tmp_a:
        tmp = 0
        for i in test_case:
            tmp += A[i]
        alice.append(tmp)
    bob.sort()
    bob_cnt = len(bob)
    for alice_value in alice:
        max_value = max(abs(alice_value-bob[0]),max_value)
        max_value = max(abs(alice_value-bob[-1]),max_value)
        left, right = 0,bob_cnt-1
        target = bob_cnt - 1
        while left <= right:
            mid = (left+right) // 2
            if bob[mid] >= alice_value:
                right = mid - 1
                target = mid
            else:
                left = mid + 1
        min_value = min(min_value,abs(bob[target]-alice_value))
        if target != 0:
            min_value = min(min_value,abs(bob[target-1]-alice_value))
        if target + 1 != bob_cnt:
            min_value = min(min_value,abs(bob[target+1]-alice_value))
    print(min_value,max_value)