#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define INF 3000000000000

using namespace std;

void dijkstra(const vector<vector<pair<int, int>>>& graph, vector<long long>& distance, int start);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;

    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n + 1, vector<pair<int, int>>());

    for (int i = 0;i < m;i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({ v,w });
        graph[v].push_back({ u,w });
    }

    int x, z;

    cin >> x >> z;

    int p;

    cin >> p;

    vector<int> pos;

    pos.push_back(x);

    for (int i = 0;i < p;i++) {
        int tmp;
        cin >> tmp;
        pos.push_back(tmp);
    }

    pos.push_back(z);

    p += 2;

    vector<vector<long long>> adj_matrix;

    for (int i = 0;i < p;i++) {
        int start = pos[i];
        vector<long long> distance(n + 1, INF);
        distance[start] = 0;
        dijkstra(graph, distance, start);
        vector<long long> tmp;
        for (int j = 0;j < p;j++) tmp.push_back(distance[pos[j]]);
        adj_matrix.push_back(tmp);
    }

    vector<vector<long long>> dp((long long)(1 << p), vector<long long>(p, INF));
    dp[1][0] = 0;

    for (int bit = 1;bit < (1 << p);bit++) {
        for (int x = 0;x < p;x++) {
            if (dp[bit][x] >= INF or (bit & (1 << x)) == 0) continue;
            int tmp = 1;
            for (int nx = 0;nx < p;nx++) {
                if ((bit & tmp) == 0) dp[bit + tmp][nx] = min(dp[bit + tmp][nx], dp[bit][x] + adj_matrix[x][nx]);
                tmp <<= 1;
            }
        }
    }

    long long answer = dp[(1 << p) - 1][p - 1];
    if (answer >= INF) answer = -1;
    cout << answer;
}

void dijkstra(const vector<vector<pair<int, int>>>& graph, vector<long long>& distance, int start) {
    priority_queue<pair<long long, int>,vector<pair<long long,int>>,greater<pair<long long, int>>> q;
    distance[start] = 0;
    q.push({ 0,start });
    while (!q.empty()) {
        pair<long long, int> tmp = q.top();
        q.pop();
        long long dist = tmp.first;
        int x = tmp.second;
        if (dist > distance[x]) continue;
        for (auto tmp : graph[x]) {
            int nx = tmp.first;
            int dd = tmp.second;
            long long nd = dist + dd;
            if (nd >= distance[nx]) continue;
            distance[nx] = nd;
            q.push({ nd,nx });
        }
    }
}