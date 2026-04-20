//https://www.acmicpc.net/source/90849267
//필자가 작성한 위 링크의 코드를 chatGPT로 변환

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct Edge {
    int to, cap, rev;
};

const int INF_NODE = 1001;          // 파이썬의 INF와 동일 (0~1000)
const int V = INF_NODE * 4;         // 각 노드는 4개의 상태를 가짐

vector<vector<Edge>> graph(V);

// 정점 u에서 v로 용량 cap의 간선을 추가 (역간선은 cap 0)
void addEdge(int u, int v, int cap) {
    graph[u].push_back({ v, cap, (int)graph[v].size() });
    graph[v].push_back({ u, 0, (int)graph[u].size() - 1 });
}

// (i, j)를 정수 id로 변환: id = i * 4 + j
int id(int i, int j) {
    return i * 4 + j;
}

// Edmonds-Karp용 BFS: source에서 sink까지의 경로를 찾고, bottleneck 값을 반환
int bfs(int s, int t, vector<int>& parent, vector<int>& parent_edge) {
    fill(parent.begin(), parent.end(), -1);
    fill(parent_edge.begin(), parent_edge.end(), -1);
    queue<pair<int, int>> q;
    q.push({ s, 1e9 });
    parent[s] = s;
    while (!q.empty()) {
        int u = q.front().first;
        int flow = q.front().second;
        q.pop();
        for (int i = 0; i < graph[u].size(); i++) {
            Edge& e = graph[u][i];
            if (parent[e.to] == -1 && e.cap > 0) {
                parent[e.to] = u;
                parent_edge[e.to] = i;
                int new_flow = min(flow, e.cap);
                if (e.to == t)
                    return new_flow;
                q.push({ e.to, new_flow });
            }
        }
    }
    return 0;
}

// 최대 유량 계산 (Edmonds-Karp)
int maxFlow(int s, int t) {
    int flow = 0;
    vector<int> parent(V), parent_edge(V);
    while (true) {
        int new_flow = bfs(s, t, parent, parent_edge);
        if (new_flow == 0)
            break;
        flow += new_flow;
        int cur = t;
        while (cur != s) {
            int prev = parent[cur];
            int edge_idx = parent_edge[cur];
            graph[prev][edge_idx].cap -= new_flow;
            int rev = graph[prev][edge_idx].rev;
            graph[cur][rev].cap += new_flow;
            cur = prev;
        }
    }
    return flow;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    // 정점 id 할당:
    // (0,0): source, (0,1): source 내부, (0,2): sink 내부, (0,3): sink
    int source = id(0, 0);         // 0
    int s_internal = id(0, 1);       // 1
    int t_internal = id(0, 2);       // 2
    int sink = id(0, 3);           // 3

    // source 내부 간선: (0,0) -> (0,1) 용량 = n+k
    addEdge(source, s_internal, n + k);
    // sink 내부 간선: (0,2) -> (0,3) 용량 = n+k
    addEdge(t_internal, sink, n + k);

    // 일자리 노드 (1 ≤ i ≤ m): (i,2)와 (i,3)
    for (int i = 1; i <= m; i++) {
        int job_entry = id(i, 2);
        int job_exit = id(i, 3);
        // 일자리 내부 간선: (i,2) -> (i,3) 용량 = 1
        addEdge(job_entry, job_exit, 1);
        // (i,3) -> (0,2) 간선: 용량 = 1
        addEdge(job_exit, t_internal, 1);
    }

    // 후보자 노드 (1 ≤ i ≤ n): (i,0)와 (i,1)
    for (int i = 1; i <= n; i++) {
        int cand_entry = id(i, 0);
        int cand_exit = id(i, 1);
        // (0,1) -> (i,0) 간선: 용량 = 2
        addEdge(s_internal, cand_entry, 2);
        // 후보자 내부 간선: (i,0) -> (i,1) 용량 = 2
        addEdge(cand_entry, cand_exit, 2);

        // 후보자가 지원할 수 있는 일자리에 대한 입력
        int cnt;
        cin >> cnt;
        for (int j = 0; j < cnt; j++) {
            int job;
            cin >> job;
            // 후보자 출구에서 해당 일자리의 entry로 간선: (i,1) -> (job,2), 용량 = 1
            addEdge(cand_exit, id(job, 2), 1);
        }
    }

    // 최대 유량 계산 – 이는 (0,0)에서 (0,3)까지의 유량이며,
    // 파이썬 코드에서 출력한 cur_flow[0][2][0][3]와 동일한 값입니다.
    int result = maxFlow(source, sink);
    cout << result << "\n";

    return 0;
}