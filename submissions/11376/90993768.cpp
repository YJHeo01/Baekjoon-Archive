//https://www.acmicpc.net/source/90993657 위 코드를 gpt로 변환

#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
using namespace std;

struct Edge {
    int nx, ny; // 도착 정점: (nx, ny)
    int cap;     // 용량
    int rev;     // 역방향 간선의 인덱스
};

// graph[x][y] : x번 정점의 y번째 레이어에서 나가는 간선 리스트 (x: 0~1000, y: 0,1,2)
vector<vector<vector<Edge>>> graph(1001, vector<vector<Edge>>(3));

// addEdge : (x,y)에서 (nx,ny)로 가는 forward edge (용량 cap)와 역방향 edge (용량 0)를 추가합니다.
void addEdge(int x, int y, int nx, int ny, int cap) {
    int forwardIndex = graph[x][y].size();
    int reverseIndex = graph[nx][ny].size();
    graph[x][y].push_back({nx, ny, cap, reverseIndex});
    graph[nx][ny].push_back({x, y, 0, forwardIndex});
}

struct Parent {
    int px, py, idx; // 이전 정점 (px,py)와 그 정점에서 사용한 간선의 인덱스
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;
    
    // 시작: (0,0)에서 (0,1)로 용량 2*n인 간선을 추가
    addEdge(0, 0, 0, 1, 2 * n);
    
    // 1부터 n까지 각 정점에 대해
    for (int i = 1; i <= n; i++){
        int t;
        cin >> t;
        // (0,1)에서 (i,0)으로 용량 2인 간선 추가
        addEdge(0, 1, i, 0, 2);
        // (i,0)에서 (i,1)으로 용량 2인 간선 추가
        addEdge(i, 0, i, 1, 2);
        // t가 0이면 더 이상 연결이 없으므로 continue
        if(t == 0) continue;
        // t개의 정점 번호 j에 대해 (i,1)에서 (j,2)로 용량 1인 간선 추가
        for (int k = 0; k < t; k++){
            int j;
            cin >> j;
            addEdge(i, 1, j, 2, 1);
        }
    }
    
    // 모든 j (1부터 1000)에 대해 (j,2)에서 (0,2)로 용량 1인 간선 추가
    for (int j = 1; j <= 1000; j++){
        addEdge(j, 2, 0, 2, 1);
    }
    
    int answer = 0;
    const int INF = 1000000000;
    
    // 최대 유량 계산 (Edmonds–Karp)
    while (true) {
        // parent 배열: 각 (x,y)마다 이전 정점과 사용한 간선 정보를 저장 (초기값: -1)
        vector<vector<Parent>> parent(1001, vector<Parent>(3, {-1, -1, -1}));
        // BFS를 위한 큐: (x, y, 현재까지의 흐름)
        queue<tuple<int, int, int>> q;
        q.push({0, 0, INF});
        parent[0][0] = {0, 0, 0};  // 시작 정점 방문 표시
        
        int flow = 0;
        while (!q.empty()){
            auto [x, y, currentFlow] = q.front();
            q.pop();
            // (x,y)에서 나가는 모든 간선에 대해
            for (int i = 0; i < graph[x][y].size(); i++){
                Edge &e = graph[x][y][i];
                int nx = e.nx, ny = e.ny;
                // 아직 방문하지 않았고 남은 용량이 있으면
                if (parent[nx][ny].px == -1 && e.cap > 0) {
                    parent[nx][ny] = {x, y, i};
                    int newFlow = min(currentFlow, e.cap);
                    // 도착지 (0,2)에 도달하면 경로상의 최소 흐름 반환
                    if (nx == 0 && ny == 2) {
                        flow = newFlow;
                        while (!q.empty()) q.pop();
                        break;
                    }
                    q.push({nx, ny, newFlow});
                }
            }
        }
        if (flow == 0) break; // 더 이상 증강 경로가 없으면 종료
        answer += flow;
        // 경로를 거슬러 올라가며 용량을 갱신
        int x = 0, y = 2;
        while (!(x == 0 && y == 0)){
            Parent p = parent[x][y];
            int px = p.px, py = p.py, idx = p.idx;
            // forward edge 용량 감소
            graph[px][py][idx].cap -= flow;
            int rev = graph[px][py][idx].rev;
            // 역방향 edge 용량 증가
            graph[x][y][rev].cap += flow;
            x = px; y = py;
        }
    }
    
    cout << answer << "\n";
    return 0;
}
