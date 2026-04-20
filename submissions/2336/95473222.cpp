#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <queue>

#define INF 987654321

using namespace std;

int score[500000][3];

int query(vector<int>& s, int node, int left, int right, int start, int end) {
    if (start > right or end < left) return INF;
    if (left <= start and end <= right) return s[node];
    int mid = (start + end) / 2;
    int ret_value = min(query(s, node * 2, left, right, start, mid), query(s, node * 2 + 1, left, right, mid + 1, end));
    return ret_value;
}

void update(vector<int>& s, int node, int target, int start, int end, int value) {
    if (start > target or end < target) return;
    if (start == end) {
        s[node] = value;
        return;
    }
    update(s, node * 2, target, start, (start + end)/2, value);
    update(s, node * 2+1, target, (start + end)/2 + 1, end, value);
    s[node] = min(s[node * 2], s[node * 2 + 1]);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;

    cin >> n;

    for (int i = 0;i < 3;i++) {
        for (int j = 0;j < n;j++) {
            int tmp;
            cin >> tmp;
            score[tmp][i] = j+1;
        }
    }

    int length = 1 << (int)(ceil(log2(n+1))+1);

    vector<int> s(length, INF);

    priority_queue<tuple<int,int,int>,vector<tuple<int,int,int>>,greater<tuple<int, int, int>>> q;

    for (int i = 1;i <= n;i++) {
        q.push({ score[i][0],score[i][1],score[i][2] });
    }

    int answer = 0;
    while (!q.empty()) {
        auto [x, y, z] = q.top();
        q.pop();
        int tmp = query(s, 1, 0, y, 0, n);
        if (tmp >= z) answer++;
        update(s, 1, y, 0, n, z);
    }

    cout << answer;

    return 0;
}