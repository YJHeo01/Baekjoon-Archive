#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <queue>

using namespace std;

long long int query(vector<int>& s, int node, int target, int start, int end) {
    if (start > target) return 0;
    if (target >= end) return s[node];
    int mid = (start + end) / 2;
    return query(s, node * 2, target, start, mid) + query(s, node * 2 + 1, target, mid + 1, end);
}

void update(vector<int>& s, int node, int target, int start, int end) {
    if (start == end) { s[node]++; return; }
    int mid = (start + end) / 2;
    if (target <= mid) update(s, node * 2, target, start, mid);
    else update(s, node * 2 + 1, target, mid + 1, end);
    s[node] = s[node * 2] + s[node * 2 + 1];
    return;
}

struct compare {
    bool operator()(const pair<int,int>& a, const pair<int,int>& b) const {
        if (a.first != b.first) return b.first > a.first;
        return a.second > b.second;
    }
};

void solution(){

    int n;
    cin >> n;

    vector<pair<int, int>> island(n);
    vector<int> x_list;
    vector<int> y_list;
    unordered_map<int, int> x_order;
    unordered_map<int, int> y_order;
    
    for (int i = 0;i < n;i++) {
        int x, y;
        cin >> x >> y;
        island[i].first = x;
        island[i].second = y;
        x_list.push_back(x);
        y_list.push_back(y);
    }
    
    sort(x_list.begin(), x_list.end());
    sort(y_list.begin(), y_list.end());
    
    x_list.erase(unique(x_list.begin(), x_list.end()), x_list.end());
    y_list.erase(unique(y_list.begin(), y_list.end()), y_list.end());
    
    for (int i = 0;i < x_list.size(); i++) x_order[x_list[i]] = i;
    for (int i = 0;i < y_list.size(); i++) y_order[y_list[i]] = i;

    int Y = y_list.size();

    priority_queue<pair<int,int>, vector<pair<int, int>>,compare> q;

    for (int i = 0;i < n;i++) {
        island[i].first = x_order[island[i].first];
        island[i].second = y_order[island[i].second];
        q.push({ island[i].first,island[i].second });
    }

    vector<int> s(4*Y, 0);

    long long int answer = 0;

    while (!q.empty()) {
        auto [x, y] = q.top();
        q.pop();
        answer += query(s, 1, y, 0, Y - 1);
        update(s, 1, y, 0, Y - 1);
    }

    cout << answer << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;

    cin >> t;

    while (t--) solution();
    return 0;
}