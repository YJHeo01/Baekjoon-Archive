#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>
#define INF 1000000

char town[50][50] = { 0, };
int high[50][50] = { 0, };
int n;
using namespace std;

int bfs(vector<vector<bool>>& visited, int x, int y, int floor, int limit, int cnt) {
    visited[x][y] = true;
    int dx[8] = { 0,1,0,-1,1,1,-1,-1 };
    int dy[8] = { 1,0,-1,0,-1,1,-1,1 };
    priority_queue<vector<int>> q;
    q.push({ -high[x][y],x,y });
    for (int ceil = floor;ceil <= limit;ceil++) {
        while (!q.empty()) {
            vector<int> tmp = q.top();
            if (-tmp[0] > ceil) break;
            int x = tmp[1];
            int y = tmp[2];
            if (town[x][y] == 'K') cnt--;
            q.pop();
            for (int i = 0;i < 8;i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]) continue;
                if (high[nx][ny] < floor) continue;
                
                visited[nx][ny] = true;
                q.push({ -high[nx][ny],nx,ny });
            }
        }
        if (cnt == 0) return ceil;
    }
    return INF;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;

    for (int i = 0;i < n;i++) cin >> town[i];

    for (int i = 0;i < n;i++) {
        for (int j = 0;j < n;j++) {
            cin >> high[i][j];
        }
    }

    int house_cnt = 0;

    int start_x = 0;
    int start_y = 0;

    int floor_high = INF;
    int ceil_min = 0;

    for (int i = 0;i < n;i++) {
        for (int j = 0;j < n;j++) {
            if (town[i][j] == '.') continue;
            ceil_min = max(high[i][j], ceil_min);
            floor_high = min(floor_high, high[i][j]);
            if (town[i][j] == 'K') house_cnt++;
            else {
                start_x = i;
                start_y = j;
            }
            
        }
    }
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    int answer = bfs(visited, start_x, start_y, 0, house_cnt, INF);

    for (int floor = floor_high;floor > 0;floor--) {
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        int tmp = bfs(visited, start_x, start_y, floor,floor+answer,house_cnt);
        answer = min(answer, tmp - floor);
    }
    cout << answer;
}