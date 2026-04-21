//https://www.acmicpc.net/source/90849267
//위 링크의 코드를 chatGPT로 변환

#include <iostream>
#include <vector>
#include <deque>
#include <utility>
using namespace std;

const int INF_NUM = 1001;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    // max_flow와 cur_flow를 INF_NUM x 4 x INF_NUM x 4 크기의 4차원 배열로 초기화 (모두 0으로)
    vector<vector<vector<vector<int>>>> max_flow(
        INF_NUM, vector<vector<vector<int>>>(
            4, vector<vector<int>>(
                INF_NUM, vector<int>(4, 0)
            )
        )
    );
    vector<vector<vector<vector<int>>>> cur_flow(
        INF_NUM, vector<vector<vector<int>>>(
            4, vector<vector<int>>(
                INF_NUM, vector<int>(4, 0)
            )
        )
    );

    // 각 정점에 대해 (x, y) 쌍을 관리하는 인접 리스트
    // graph[x][y]에는 (nx, ny)로 갈 수 있는 인접 정점들이 저장됨
    vector<vector<vector<pair<int, int>>>> graph(
        INF_NUM, vector<vector<pair<int, int>>>(4)
    );

    // source와 sink 내부 간선
    // source: (0,0) → (0,1), sink: (0,2) → (0,3) (용량: n+k)
    max_flow[0][0][0][1] = n + k;
    max_flow[0][2][0][3] = n + k;

    graph[0][0].push_back({ 0, 1 });
    graph[0][1].push_back({ 0, 0 });
    graph[0][2].push_back({ 0, 3 });
    graph[0][3].push_back({ 0, 2 });

    // 일자리 노드 (1 ≤ i ≤ m)
    for (int i = 1; i <= m; i++) {
        // (i,2) → (i,3) 간선: 용량 1
        // (i,3) → (0,2) 간선: 용량 1
        max_flow[i][2][i][3] = 1;
        max_flow[i][3][0][2] = 1;

        graph[i][2].push_back({ i, 3 });
        graph[i][3].push_back({ i, 2 });
        graph[0][2].push_back({ i, 3 });
        graph[i][3].push_back({ 0, 2 });
    }

    // 후보자 노드 (1 ≤ i ≤ n)
    for (int i = 1; i <= n; i++) {
        // (0,1) → (i,0): 용량 2, 그리고 후보자 내부 간선 (i,0) → (i,1): 용량 2
        graph[0][1].push_back({ i, 0 });
        graph[i][0].push_back({ 0, 1 });
        max_flow[0][1][i][0] = 2;
        max_flow[i][0][i][1] = 2;
        graph[i][0].push_back({ i, 1 });
        graph[i][1].push_back({ i, 0 });

        int cnt;
        cin >> cnt;
        if (cnt == 0) continue;
        // 후보자가 지원하는 일자리에 대해 (i,1) → (job,2) 간선 (용량 1)
        for (int j = 0; j < cnt; j++) {
            int job;
            cin >> job;
            max_flow[i][1][job][2] = 1;
            graph[i][1].push_back({ job, 2 });
            graph[job][2].push_back({ i, 1 });
        }
    }

    // 증강 경로를 찾는 while문 (BFS 이용)
    while (true) {
        // 각 정점 (x, y)마다 이전 정점을 저장 (초기값: (-1,-1))
        vector<vector<pair<int, int>>> prev(
            INF_NUM, vector<pair<int, int>>(4, { -1, -1 })
        );
        deque<pair<int, int>> dq;
        dq.push_back({ 0, 0 });  // 시작점: (0,0)

        // (0,3)이 sink
        while (!dq.empty() && prev[0][3].first == -1) {
            auto [x, y] = dq.front();
            dq.pop_front();
            // 인접 정점 탐색
            for (auto& p : graph[x][y]) {
                int nx = p.first, ny = p.second;
                // 잔여 용량이 남아있고 아직 방문하지 않은 경우
                if (max_flow[x][y][nx][ny] > cur_flow[x][y][nx][ny] && prev[nx][ny].first == -1) {
                    dq.push_back({ nx, ny });
                    prev[nx][ny] = { x, y };
                    if (nx == 0 && ny == 3) break;  // sink에 도달하면 종료
                }
            }
        }

        // sink에 도달하지 못한 경우 while문 종료
        if (prev[0][3].first == -1) break;

        // 찾은 경로에 대해 flow 1을 흘려보냄
        int flow = 1;
        int x = 0, y = 3;
        while (!(x == 0 && y == 0)) {
            int px = prev[x][y].first, py = prev[x][y].second;
            cur_flow[px][py][x][y] += flow;
            cur_flow[x][y][px][py] -= flow;
            x = px;
            y = py;
        }
    }

    // 결과는 cur_flow[0][2][0][3]에 저장된 값 (sink 내부 간선의 유량)
    std::cout << cur_flow[0][2][0][3] << "\n";

    return 0;
}