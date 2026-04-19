#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#define INF 1000000

char town[50][50] = { 0, };
int high[50][50] = { 0, };
int n;
using namespace std;

int bfs(vector<vector<bool>>& visited, int x, int y, int ceil, int floor) {
    int ret_value = 0;
    visited[x][y] = true;
    int dx[8] = { 0,1,0,-1,1,1,-1,-1 };
    int dy[8] = { 1,0,-1,0,-1,1,-1,1 };
    queue<pair<int, int>> q;
    q.push({ x,y });
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0;i < 8;i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]) continue;
            if (high[nx][ny] > ceil or high[nx][ny] < floor) continue;
            if (town[nx][ny] == 'K') ret_value++;
            visited[nx][ny] = true;
            q.push({ nx,ny });
        }
    }
    return ret_value;
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

    int answer = INF;

    for (int floor = 0;floor <= floor_high;floor++) {
        int left = ceil_min;
        int right = min(INF, floor + answer);
        while (left <= right) {
            int mid = (left + right) / 2;
            vector<vector<bool>> visited(n, vector<bool>(n, false));
            if (house_cnt == bfs(visited, start_x, start_y, mid, floor)) {
                answer = min(answer, mid - floor);
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
    }
    cout << answer;
}