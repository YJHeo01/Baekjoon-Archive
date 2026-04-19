#include <queue>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int dfs(vector<vector<pair<int, int>>> graph, vector<int> dist, int x) {
    int ret_value = dist[x];
    for (auto& p : graph[x]) {
        auto nx = p.first;
        auto d = p.second;
        if (dist[nx] != -1) continue;
        dist[nx] = dist[x] + d;
        ret_value = max(ret_value, dfs(graph, dist, nx));
    }
    return ret_value;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<vector<pair<int, int>>> graph(10001);
    while (true) {
        int a, b, c;
        cin >> a >> b >> c;
        if (cin.eof() == true) break;
        graph[a].push_back({ b,c });
        graph[b].push_back({ a,c });
    }
    int answer = 0;
    for (int i = 1;i <= 10000;i++) {
        vector<int> dist(10001, -1);
        dist[i] = 0;
        answer = max(answer, dfs(graph, dist, i));
    }
    cout << answer;
}