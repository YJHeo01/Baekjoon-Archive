#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    int n, k, s;
    cin >> n >> k >> s;
    if (k >= 37) {
        cout << "MEGA" << endl;
        return 0;
    }
    vector<int> array(n);
    for (int i = 0; i < n; ++i) {
        cin >> array[i];
    }
    vector<vector<long long>> dp(n + 1, vector<long long>(k + 1, 0));
    dp[0][0] = s;
    priority_queue<pair<long long, pair<int, int>>> q;
    q.push({ -s, {0, 0} });
    while (!q.empty()) {
        long long vd = q.top().first;
        int vx = q.top().second.first;
        int vy = q.top().second.second;
        q.pop();
        vd *= -1;
        if (dp[vx][vy] > vd || dp[vx][vy] <= 0 || vx == n) continue;
        long long nd = vd + array[vx];
        int nx = vx + 1, ny = vy;
        if (nd > dp[nx][ny]) {
            dp[nx][ny] = nd;
            q.push({ -nd, {nx, ny} });
        }
        if (vy == k) continue;
        nd = vd * 2;
        nx = vx + 1; ny = vy + 1;
        if (nd > dp[nx][ny]) {
            dp[nx][ny] = nd;
            q.push({ -nd, {nx, ny} });
        }
    }
    long long answer = *max_element(dp[n].begin(), dp[n].end());
    if (answer > 100000000000LL) {
        cout << "MEGA" << endl;
    }
    else if (answer <= 0) {
        cout << "-1" << endl;
    }
    else {
        cout << answer << endl;
    }
    return 0;
}