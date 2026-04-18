//https://www.acmicpc.net/source/100702072 해당 제출을 AI를 이용하여 python -> C++ 변환

#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000;
int h, w;
int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};

int dijk(const vector<string> &graph, vector<vector<int>> &dist, int sx, int sy) {
    int ret_value = INF;
    dist[sx][sy] = 0;

    using T = tuple<int,int,int>; // (cnt, x, y)
    priority_queue<T, vector<T>, greater<T>> pq;
    pq.push({0, sx, sy});

    while (!pq.empty()) {
        auto [cnt, x, y] = pq.top();
        pq.pop();

        if (cnt > dist[x][y]) continue;
        if (graph[x][y] == '#') cnt++;

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || ny < 0 || nx >= h || ny >= w) {
                ret_value = min(ret_value, cnt);
                continue;
            }
            if (graph[nx][ny] == '*' || cnt >= dist[nx][ny]) continue;

            dist[nx][ny] = cnt;
            pq.push({cnt, nx, ny});
        }
    }
    return ret_value;
}

int solution() {
    cin >> h >> w;
    vector<string> maze(h);
    for (int i = 0; i < h; i++) {
        cin >> maze[i];
    }

    pair<int,int> trash_1(-1, -1), trash_2(-1, -1);

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (maze[i][j] != '$') continue;
            if (trash_1.first == -1) trash_1 = {i, j};
            else trash_2 = {i, j};
        }
    }

    deque<pair<int,int>> dq;
    dq.push_back(trash_1);
    dq.push_back(trash_2);

    vector<vector<bool>> visited(h, vector<bool>(w, false));
    int answer = h * w;

    // 첫 BFS
    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();
        visited[x][y] = true;

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || ny < 0 || nx >= h || ny >= w) return 0;
            if (visited[nx][ny] || maze[nx][ny] == '#' || maze[nx][ny] == '*') continue;

            visited[nx][ny] = true;
            dq.push_back({nx, ny});
        }
    }

    // 가장자리 체크
    for (int i = 0; i < h; i++) {
        if (visited[i][w - 1] || visited[i][0]) {
            answer = 0;
            break;
        }
    }
    for (int i = 0; i < w && answer != 0; i++) {
        if (visited[0][i] || visited[h - 1][i]) {
            answer = 0;
            break;
        }
    }
    if (answer == 0) return answer;

    // 첫 번째 죄수 다익스트라
    vector<vector<int>> a_dist(h, vector<int>(w, INF));
    using T = tuple<int,int,int>;
    priority_queue<T, vector<T>, greater<T>> pq;

    a_dist[trash_1.first][trash_1.second] = 0;
    pq.push({0, trash_1.first, trash_1.second});

    while (!pq.empty()) {
        auto [cnt, x, y] = pq.top();
        pq.pop();
        if (cnt > a_dist[x][y]) continue;
        int ncnt = cnt;
        if (maze[x][y] == '#') ncnt++;

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
            if (maze[nx][ny] == '*' || ncnt >= a_dist[nx][ny]) continue;

            a_dist[nx][ny] = ncnt;
            pq.push({ncnt, nx, ny});
        }
    }

    // 두 번째 죄수 다익스트라
    vector<vector<int>> b_dist(h, vector<int>(w, INF));
    while (!pq.empty()) pq.pop();

    b_dist[trash_2.first][trash_2.second] = 0;
    pq.push({0, trash_2.first, trash_2.second});

    while (!pq.empty()) {
        auto [cnt, x, y] = pq.top();
        pq.pop();
        if (cnt > b_dist[x][y]) continue;
        int ncnt = cnt;
        if (maze[x][y] == '#') ncnt++;

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
            if (maze[nx][ny] == '*' || ncnt >= b_dist[nx][ny]) continue;

            b_dist[nx][ny] = ncnt;
            pq.push({ncnt, nx, ny});
        }
    }

    // 문(‘#’)들에 대해 탐색
    for (int x = 0; x < h; x++) {
        for (int y = 0; y < w; y++) {
            if (maze[x][y] != '#') continue;

            int tmp = 1;
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (nx < 0 || ny < 0 || nx >= h || ny >= w ||
                    maze[nx][ny] == '.' || maze[nx][ny] == '$')
                    tmp = 0;
            }

            if (tmp || visited[x][y] ||
                a_dist[x][y] + b_dist[x][y] + 1 >= answer)
                continue;

            vector<vector<int>> dist(h, vector<int>(w, INF));
            int d = dijk(maze, dist, x, y);
            answer = min(answer, a_dist[x][y] + b_dist[x][y] + d);

            deque<pair<int,int>> qq;
            qq.push_back({x, y});
            while (!qq.empty()) {
                auto [cx, cy] = qq.front();
                qq.pop_front();
                for (int k = 0; k < 4; k++) {
                    int nx = cx + dx[k];
                    int ny = cy + dy[k];
                    if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
                    if (visited[nx][ny] || maze[nx][ny] != '#') continue;
                    visited[nx][ny] = true;
                    qq.push_back({nx, ny});
                }
            }
        }
    }

    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        cout << solution() << '\n';
    }
    return 0;
}

