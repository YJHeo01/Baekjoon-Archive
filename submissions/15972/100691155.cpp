//이전에 작성하였던 https://www.acmicpc.net/source/89902170의 코드를 생성형 AI를 이용해서 C++로 변환

#include <bits/stdc++.h>
using namespace std;

int n, m, h;

struct Node {
    int high;
    int tmp;
    int x;
    int y;
};

struct Cmp {
    bool operator()(const Node& a, const Node& b) const {
        if (a.high != b.high) return a.high > b.high;  // min-heap by high
        if (a.tmp  != b.tmp)  return a.tmp  > b.tmp;
        if (a.x    != b.x)    return a.x    > b.x;
        return a.y > b.y;
    }
};

void print_water(const vector<vector<int>>& water) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << water[i][j] << ' ';
        }
        cout << '\n';
    }
    cout << '\n';
}

void solution(const vector<vector<int>>& row_block,
              const vector<vector<int>>& column_block,
              vector<vector<int>>& water) {
    priority_queue<Node, vector<Node>, Cmp> q;

    // 위/아래 테두리
    for (int i = 0; i < m; ++i) {
        if (row_block[0][i] != -1 && water[0][i] > row_block[0][i]) {
            water[0][i] = row_block[0][i];
            q.push({water[0][i], 0, 0, i});
        }
        if (row_block[n][i] != -1 && water[n-1][i] > row_block[n][i]) {
            water[n-1][i] = row_block[n][i];
            q.push({water[n-1][i], 0, n-1, i});
        }
    }

    // 왼/오 테두리
    for (int i = 0; i < n; ++i) {
        if (column_block[i][0] != -1 && water[i][0] > column_block[i][0]) {
            water[i][0] = column_block[i][0];
            q.push({water[i][0], 0, i, 0});
        }
        if (column_block[i][m] != -1 && water[i][m-1] > column_block[i][m]) {
            water[i][m-1] = column_block[i][m];
            q.push({water[i][m-1], 0, i, m-1});
        }
    }
    // print_water(water);

    const int dx[4] = {0, 0, 1, -1};
    const int dy[4] = {1, -1, 0, 0};

    while (!q.empty()) {
        Node cur = q.top();
        q.pop();
        int high = cur.high;
        int vx = cur.x;
        int vy = cur.y;

        if (high > water[vx][vy]) continue;

        for (int dir = 0; dir < 4; ++dir) {
            int nx = vx + dx[dir];
            int ny = vy + dy[dir];

            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

            int hole_high;
            if (dy[dir] == 0) {
                // 위/아래 이동 → row_block 사용
                int block_x, block_y;
                if (dx[dir] == 1) { // 아래로
                    block_x = nx;
                    block_y = ny;
                } else {            // 위로
                    block_x = vx;
                    block_y = vy;
                }
                hole_high = row_block[block_x][block_y];
            } else {
                // 좌/우 이동 → column_block 사용
                int block_x, block_y;
                if (dy[dir] == 1) { // 오른쪽
                    block_x = nx;
                    block_y = ny;
                } else {            // 왼쪽
                    block_x = vx;
                    block_y = vy;
                }
                hole_high = column_block[block_x][block_y];
            }

            if (hole_high == -1) continue;

            int next_high = max(hole_high, water[vx][vy]);
            if (water[nx][ny] > next_high) {
                water[nx][ny] = next_high;
                q.push({next_high, next_high - hole_high, nx, ny});
            }
        }
    }
    // print_water(water);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> h;

    // Python:
    // row_block = [list(map(int,input().split())) for _ in range(n+1)]
    // column_block = [list(map(int,input().split())) for _ in range(n)]
    vector<vector<int>> row_block(n + 1, vector<int>(m));
    vector<vector<int>> column_block(n, vector<int>(m + 1));

    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> row_block[i][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= m; ++j) {
            cin >> column_block[i][j];
        }
    }

    vector<vector<int>> water(n, vector<int>(m, h));

    solution(row_block, column_block, water);

    long long answer = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            answer += water[i][j];

    cout << answer << '\n';
    return 0;
}
