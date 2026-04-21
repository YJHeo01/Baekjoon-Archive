#define INF 987654321

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int arr[1000][1000] = { 0, };
int dist[1000][1000] = { 0, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n;
    cin >> m >> n;
    
    for (int i = 0;i < m;i++) {
        for (int j = 0;j < n;j++) {
            cin >> arr[i][j];
            dist[i][j] = INF;
        }
    }

    dist[0][0] = arr[0][0];
    if (arr[0][0] == -1) {
        cout << -1;
        return 0;
    }

    priority_queue<tuple<int, int, int>,vector<tuple<int,int,int>>,greater<tuple<int,int,int>>> q;

    q.emplace(dist[0][0], 0, 0);

    int dx[4] = { 0,1,0,-1 };
    int dy[4] = { 1,0,-1,0 };
    
    while (!q.empty()) {
        auto [d, x, y] = q.top(); q.pop();
        if (d > dist[x][y]) continue;
        for (int i = 0;i < 4;i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 or ny < 0 or nx >= m or ny >= n or arr[nx][ny] == -1) continue;
            int nd = d + arr[nx][ny];
            if (dist[nx][ny] > nd) {
                dist[nx][ny] = nd;
                q.emplace(nd, nx, ny);
            }

        }
    }

    int answer = dist[m - 1][n - 1];
    if (answer >= INF) answer = -1;
    cout << answer;

    return 0;
}
