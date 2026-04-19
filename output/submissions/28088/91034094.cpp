#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;
    vector<int> cur(n, 0);

    for (int i = 0;i < m;i++) {
        int tmp;
        cin >> tmp;
        cur[tmp] = 1;
    }

    for (int i = 0;i < k;i++) {
        vector<int> next(n, 0);
        for (int j = 0;j < n;j++) {
            cur[j] %= 2;
            if (cur[j] == 0) continue;
            for (int dx : {-1, 1}) next[(j + dx+n) % n]++;
        }
        cur = next;
    }
    int answer = 0;
    for (int x : cur) answer += (x % 2);
    cout << answer;
}