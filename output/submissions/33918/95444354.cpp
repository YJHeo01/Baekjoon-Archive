#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>

#define INF 987654321

using namespace std;

int dp[201][25001] = { 0, };

void init(vector<int>& a, vector<int>& s, int node, int start, int end);
int query(vector<int>& s, int node, int left, int right, int start, int end);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m, c, d;

    cin >> n >> m >> c >> d;

    int target[200] = { 0, };

    for (int i = 0;i < n;i++) {
        int tmp;
        cin >> tmp;
        target[i] = tmp;
    }

    for (int time = 0;time < n;time++) {
        for (int i = 1;i <= c;i++) {
            vector<int> a;
            for (int j = i;j <= m;j += c) {
                a.push_back(dp[time][j]);
            }
            int length = a.size();
            vector<int> s(2 << (int)ceil(log2(length)));
            init(a, s, 1, 0, length - 1);
            for (int j = 0;j < length;j++) {
                dp[time + 1][j * c + i] = query(s, 1, max(0, j - d / c), min(length - 1, j + d / c), 0, length - 1);
                dp[time + 1][j * c + i] += (m - abs(target[time] - (j * c + i)));
            }
        }
    }

    int answer = 0;

    for (int i = 1;i <= m;i++) answer = max(answer, dp[n][i]);

    cout << answer;

    return 0;
}

void init(vector<int>& a, vector<int>& s, int node, int start, int end) {
    if (start == end) {
        s[node] = a[end];
        return;
    }
    int mid = (start + end) / 2;
    init(a, s, node * 2, start, mid);
    init(a, s, node * 2 + 1, mid + 1, end);
    s[node] = max(s[node * 2], s[node * 2 + 1]);
}

int query(vector<int>& s, int node, int left, int right, int start, int end) {
    if (left <= start and end <= right) return s[node];
    if (left > end or right < start) return -INF;
    int mid = (start + end) / 2;
    int ret_value = max(query(s, node * 2, left, right, start, mid), query(s, node * 2 + 1, left, right, mid + 1, end));
    return ret_value;
}
