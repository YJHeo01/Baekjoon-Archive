#include <iostream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;

    cin >> n >> q;

    vector<set<int>> S(n + 1);

    for (int i = 1;i <= n;i++) {
        int n_i;
        cin >> n_i;
        for (int j = 0;j < n_i;j++) {
            int tmp;
            cin >> tmp;
            S[i].insert(tmp);
        }
    }

    for (int i = 0;i < q;i++) {
        int command;
        cin >> command;
        if (command == 1) {
            int a, b;
            cin >> a >> b;
            if (S[a].size() < S[b].size()) swap(S[a], S[b]);
            S[a].merge(S[b]);
            S[b].clear();
        }
        else {
            int a;
            cin >> a;
            cout << S[a].size() << "\n";
        }
    }
    return 0;
}