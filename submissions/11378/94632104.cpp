//https://www.acmicpc.net/source/94631327를 GPT로 변환
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to;     // 상대 정점 (flattened id)
    int cap;    // 남은 용량
    int rev;    // 역방향 간선의 인덱스
};

vector<Edge> G[5000];  // 충분히 큰 크기: (n + m + 2) * 4 <= 약 4,008

// u → v 로 향하는 용량 cap 간선을 추가합니다.
// 내부적으로 G[v]에 (v→u, 0)인 역방향 간선도 함께 생성됩니다.
void add_edge(int u, int v, int cap) {
    G[u].push_back(Edge{v, cap, (int)G[v].size()});
    G[v].push_back(Edge{u, 0,   (int)G[u].size() - 1});
}

// (node, layer) 쌍을 단일 정점 ID로 매핑합니다.
inline int id(int node, int layer) {
    return node * 4 + layer;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    // 전체 정점 수 계산
    int V = (n + m + 2) * 4;
    int S = id(0, 0);
    int T = id(0, 3);

    // super-source → (0,1) : n + k
    add_edge(id(0,0), id(0,1), n + k);

    // 직원 노드들 (1..n)
    for(int i = 1; i <= n; i++){
        int cap, cntJobs;
        cin >> cap;
        // cap : i번 직원이 할 수 있는 최대 일 수
        // tmp[1..] : 이 직원이 지원 가능한 job 리스트
        vector<int> jobs(cap);
        for(int j = 0; j < cap; j++){
            cin >> jobs[j];
        }

        // (0,1) → (i,0) : 용량 = tmp[0]
        add_edge(id(0,1), id(i,0), cap);
        // 직원 분할 : (i,0) → (i,1) : 용량 = k + 1
        add_edge(id(i,0), id(i,1), k + 1);
        // 직원 → job 연결: (i,1) → (job,2) : 용량 = 1
        for(int job : jobs){
            add_edge(id(i,1), id(job,2), 1);
        }
    }

    // job 노드들 (1..m)
    for(int j = 1; j <= m; j++){
        // job 분할 : (j,2) → (j,3) : 용량 = 1
        add_edge(id(j,2), id(j,3), 1);
        // job → super-sink 분기: (j,3) → (0,2) : 용량 = 1
        add_edge(id(j,3), id(0,2), 1);
    }

    // super-sink 분할 : (0,2) → (0,3) : 용량 = m
    add_edge(id(0,2), id(0,3), m);

    // Edmonds–Karp (BFS 기반 증강 경로)
    int max_flow = 0;
    while(true){
        vector<pair<int,int>> prev(V, {-1,-1});
        queue<int> q;
        q.push(S);
        prev[S] = {-2, -1};  // 시작점 표시

        // BFS로 증강 경로 탐색
        while(!q.empty() && prev[T].first == -1){
            int u = q.front(); q.pop();
            for(int i = 0; i < (int)G[u].size(); i++){
                Edge &e = G[u][i];
                if(e.cap > 0 && prev[e.to].first == -1){
                    prev[e.to] = {u, i};
                    q.push(e.to);
                    if(e.to == T) break;
                }
            }
        }
        if(prev[T].first == -1) break;  // 더 이상 경로 없음

        // 경로 중 최소 잔여용량 계산
        int flow = INT_MAX;
        for(int v = T; v != S; v = prev[v].first){
            auto [pu, pi] = prev[v];
            flow = min(flow, G[pu][pi].cap);
        }
        // 용량 갱신
        for(int v = T; v != S; v = prev[v].first){
            auto [pu, pi] = prev[v];
            Edge &e = G[pu][pi];
            e.cap -= flow;
            G[v][e.rev].cap += flow;
        }
        max_flow += flow;
    }

    cout << max_flow << "\n";
    return 0;
}
