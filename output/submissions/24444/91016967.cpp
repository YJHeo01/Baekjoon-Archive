#include <queue>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void bfs(vector<vector<int>>& graph, vector<int> &visited, int start) {
    queue<int> q;
    int order = 2;
    visited[start] = 1;
    q.push(start);
    while (!q.empty()) {
        int x = q.front();
        q.pop();
        for (auto nx : graph[x]) {
            if (visited[nx] != 0) continue;
            visited[nx] = order++;
            q.push(nx);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, r;
    cin >> n >> m >> r;
    vector<vector<int>> graph(n+1);
    int u, v;
    for (int i = 0;i < m;i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    for (int i = 1;i <= n;i++) sort(graph[i].begin(), graph[i].end());
    vector<int> visited(n+1, 0);
    bfs(graph, visited, r);
    for (int i = 1;i <= n;i++) cout << visited[i] << '\n';
}