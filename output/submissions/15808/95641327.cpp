#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define INF 987654321

int adj_matrix[1001][1001] = { 0, };

int tour[1001] = { 0, };
int hotel[1001] = { 0, };

using namespace std;

int dijkstra(int start) {
    int distance[1001] = { 0, };
    int ret_value = -INF;
    fill(distance,distance+1001,INF);
    distance[start] = 0;
    priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int, int>>> q;
    q.push({ 0,start });
    while (!q.empty()) {
        pair<int, int> tmp = q.top();
        q.pop();
        int dist = tmp.first;
        int x = tmp.second;
        if (dist != distance[x]) continue;
        if (hotel[x] != 0) ret_value = max(ret_value, hotel[x] - distance[x]);
        for (int nx = 1;nx <= 1000;nx++) {
            if (adj_matrix[x][nx] == 0) continue;
            int nd = dist + adj_matrix[x][nx];
            if (distance[nx] > nd) {
                distance[nx] = nd;
                q.push({ nd,nx });
            }
        }
    }
    return ret_value;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;

    cin >> n;

    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= n;j++) {
            int tmp;
            cin >> tmp;
            adj_matrix[i][j] = tmp;
        }
    }

    int p, q;

    cin >> p >> q;

    for (int i = 0;i < p;i++) {
        int l, w;
        cin >> l >> w;
        tour[l] = w;
    }

    for (int i = 0;i < q;i++) {
        int l, w;
        cin >> l >> w;
        hotel[l] = w;
    }

    int answer = -9876545321;
    
    for (int i = 1;i <= n;i++) {
        if (tour[i] == 0) continue;
        answer = max(answer, tour[i] + dijkstra(i));
    }

    cout << answer;

    return 0;
}