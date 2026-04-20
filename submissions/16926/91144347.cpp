#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, r;
    cin >> n >> m >> r;
    vector<pair<pair<int, int>, pair<int, int>>> pos;
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    int x, y;

    x = 0;
    y = m - 1;

    int dx[4] = { 0,1,0,-1 };
    int dy[4] = { -1,0,1,0 };

    while (1) {
        if (visited[x][y] == true) break;
        for (int i = 0;i < 4;i++) {
            while (1) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]) break;
                visited[nx][ny] = true;
                pos.push_back({ {x,y},{nx,ny} });
                x = nx;
                y = ny;
            }
        }
        x += 1;
        y -= 1;
    }

    vector<vector<int>> arr(n, vector<int>(m, 0));

    for (int i = 0;i < n;i++) {
        for (int j = 0;j < m;j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0;i < r;i++) {
        vector<vector<int>> new_arr(n, vector<int>(m, 0));
        for (auto tmp : pos) {
            pair<int, int> cur = tmp.first;
            pair<int, int> next = tmp.second;
            new_arr[next.first][next.second] = arr[cur.first][cur.second];
        }
        arr = new_arr;
    }

    for (auto line : arr) {
        for (auto value : line) {
            cout << value << " ";
        }
        cout << "\n";
    }
}