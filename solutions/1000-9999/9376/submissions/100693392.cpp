//https://www.acmicpc.net/source/100693269 코드를 생성형 AI를 이용해서 python -> cpp로 변환

#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

int h, w;
int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};

int dijk(const vector<string> &graph, int sx, int sy) {
    int ret_value = INF;
    vector<vector<int>> dist(h, vector<int>(w, INF));
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<tuple<int,int,int>>> pq;

    dist[sx][sy] = 0;
    pq.emplace(0, sx, sy);

    while (!pq.empty()) {
        auto [cnt, x, y] = pq.top();
        pq.pop();

        if (cnt > dist[x][y]) continue;
        if (graph[x][y] == '#') cnt++;

        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx < 0 || ny < 0 || nx >= h || ny >= w) {
                ret_value = min(ret_value, cnt);
                continue;
            }

            if (graph[nx][ny] == '*' || cnt >= dist[nx][ny]) continue;
            dist[nx][ny] = cnt;
            pq.emplace(cnt, nx, ny);
        }
    }

    return ret_value;
}

int solution() {
    cin >> h >> w;
    vector<string> maze(h);
    for (int i = 0; i < h; ++i) {
        cin >> maze[i];
    }

    pair<int,int> trash_1 = {-1, -1};
    pair<int,int> trash_2 = {-1, -1};

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (maze[i][j] != '$') continue;
            if (trash_1.first == -1) trash_1 = {i, j};
            else trash_2 = {i, j};
        }
    }

    deque<pair<int,int>> q;
    // Python 코드 그대로: 두 prisoner를 시작점으로 BFS
    q.push_back(trash_1);
    q.push_back(trash_2);

    vector<vector<bool>> visited(h, vector<bool>(w, false));
    int answer = h * w;

    // BFS 부분
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop_front();

        visited[x][y] = true;

        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx < 0 || ny < 0 || nx >= h || ny >= w) return 0;
            if (visited[nx][ny] || maze[nx][ny] == '#' || maze[nx][ny] == '*') continue;
            visited[nx][ny] = true;
            q.emplace_back(nx, ny);
        }
    }

    for (int i = 0; i < h; ++i) {
        if (visited[i][w - 1] || visited[i][0]) {
            answer = 0;
            break;
        }
    }

    for (int i = 0; i < w; ++i) {
        if (visited[0][i] || visited[h - 1][i]) {
            answer = 0;
            break;
        }
    }

    if (answer == 0) {
        return answer;
    }

    // a_dist: 첫 번째 prisoner 기준 Dijkstra
    vector<vector<int>> a_dist(h, vector<int>(w, INF));
    a_dist[trash_1.first][trash_1.second] = 0;

    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<tuple<int,int,int>>> pq;
    pq.emplace(0, trash_1.first, trash_1.second);

    while (!pq.empty()) {
        auto [cnt, x, y] = pq.top();
        pq.pop();

        if (a_dist[x][y] < cnt) continue;

        int nc = cnt;
        if (maze[x][y] == '#') nc++;

        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
            if (maze[nx][ny] == '*' || nc >= a_dist[nx][ny]) continue;

            a_dist[nx][ny] = nc;
            pq.emplace(nc, nx, ny);
        }
    }

    // b_dist: 두 번째 prisoner 기준 Dijkstra
    vector<vector<int>> b_dist(h, vector<int>(w, INF));
    b_dist[trash_2.first][trash_2.second] = 0;

    pq.emplace(0, trash_2.first, trash_2.second);

    while (!pq.empty()) {
        auto [cnt, x, y] = pq.top();
        pq.pop();

        if (cnt > b_dist[x][y]) continue;

        int nc = cnt;
        if (maze[x][y] == '#') nc++;

        for (int dir = 0; dir < 4; ++dir) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
            if (maze[nx][ny] == '*' || nc >= b_dist[nx][ny]) continue;

            b_dist[nx][ny] = nc;
            pq.emplace(nc, nx, ny);
        }
    }

    // 각 문('#')에 대해 추가 Dijkstra 호출
    for (int x = 0; x < h; ++x) {
        for (int y = 0; y < w; ++y) {
            if (maze[x][y] != '#') continue;

            int tmp = 1;
            for (int dir = 0; dir < 4; ++dir) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                if (nx < 0 || ny < 0 || nx >= h || ny >= w ||
                    maze[nx][ny] == '.' || maze[nx][ny] == '$') {
                    tmp = 0;
                }
            }

            if (tmp || (a_dist[x][y] + b_dist[x][y] + 1) >= answer) continue;

            int extra = dijk(maze, x, y);
            answer = min(answer, a_dist[x][y] + b_dist[x][y] + extra);
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
