#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    vector<int> queries(T);
    int maxN = 0;
    for (int i = 0; i < T; ++i) {
        cin >> queries[i];
        if (queries[i] > maxN) maxN = queries[i];
    }

    vector<long long> num_list;
    num_list.reserve(maxN);

    priority_queue<
        long long,
        vector<long long>,
        greater<long long>
    > pq;

    unordered_set<long long> exist;
    pq.push(1);
    exist.insert(1);

    while (static_cast<int>(num_list.size()) < maxN) {
        long long x = pq.top();
        pq.pop();
        num_list.push_back(x);

        for (long long mul : {2, 3}) {
            long long nx = x * mul + 1;
            if (exist.insert(nx).second) {   // true if nx was not present
                pq.push(nx);
            }
        }
    }

    for (int n : queries) {
        cout << num_list[n - 1] << '\n';
    }
    return 0;
}
