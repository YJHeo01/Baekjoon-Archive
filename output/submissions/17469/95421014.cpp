#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <string>
#include <stack>
#include <set>

#define INF 987654321

using namespace std;

int find_parent(vector<int>& root, int x) {
    if (root[x] != x) {
        root[x] = find_parent(root, root[x]);
    }
    return root[x];
}

int union_parent(vector<int>& root, vector<set<int>>& color, int a, int b) {
    a = find_parent(root, a);
    b = find_parent(root, b);
    if (color[a].size() > color[b].size()) {
        swap(color[a], color[b]);
    }
    root[a] = b;
    for (auto i : color[a]) {
        color[b].insert(i);
    }
    return 0;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;

    cin >> n >> q;

    vector<int> parent(2);

    for (int i = 1;i < n;i++) {
        int tmp;
        cin >> tmp;
        parent.push_back(tmp);
    }

    vector<set<int>> color(n+1);

    for (int i = 1;i <= n;i++) {
        int tmp;
        cin >> tmp;
        color[i].insert(tmp);
    }
    
    stack<pair<int, int>> s;

    for (int i = 0;i < n-1+q;i++) {
        int command, a;
        cin >> command >> a;
        s.push({ command,a });
    }

    vector<int> root(n + 1);

    for (int i = 1;i <= n;i++) {
        root[i] = i;
    }

    stack<int> answer;

    while (!s.empty()) {
        auto [command, a] = s.top();
        s.pop();
        if (command == 1) {
            union_parent(root, color, a, parent[a]);
        }
        else {
            answer.push(color[find_parent(root,a)].size());
        }
    }

    while (!answer.empty()) {
        int tmp = answer.top();
        answer.pop();
        cout << tmp << "\n";
    }

    return 0;
}
