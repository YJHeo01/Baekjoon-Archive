/*
n,m = map(int,input().split())

num_list = []

num_list.append((0,1))
num_list.append((1,1))

def Euclidean(a,b):
    if b == 0: return a
    return Euclidean(b,a%b)

for i in range(2,n+1):
    for j in range(i):
        tmp = Euclidean(i,j)
        if tmp == 1:
            num_list.append((j,i))

num_list.sort(key=lambda x:x[0]/x[1])

m -= 1

print(*num_list[m])
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    vector<pair<long long, long long>> num_list;
    num_list.emplace_back(0, 1);
    num_list.emplace_back(1, 1);

    auto gcd_ll = [](long long a, long long b) {
        while (b) {
            long long t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    for (long long i = 2; i <= n; ++i) {
        for (long long j = 0; j < i; ++j) {
            if (gcd_ll(i, j) == 1) {
                num_list.emplace_back(j, i);
            }
        }
    }

    sort(num_list.begin(), num_list.end(),
         [](const pair<long long, long long>& x,
            const pair<long long, long long>& y) {
             // x.first/x.second < y.first/y.second ?
             __int128 lhs = (__int128)x.first * y.second;
             __int128 rhs = (__int128)y.first * x.second;
             return lhs < rhs;
         });

    --m; // 1-based -> 0-based
    cout << num_list[m].first << ' ' << num_list[m].second << '\n';
    return 0;
}
