#include <iostream>

#include <vector>

#include <queue>

#include <algorithm>

using namespace std;

const int INF = 1000000000;

struct Edge {

    int v, l, r;

};

// min_size가 주어졌을 때, 1번 정점에서 시작하여

// 조건(min_size가 간선의 [l, r] 범위 내에 있을 때)으로 이동하면서

// 각 정점에 도달할 때까지의 "최소 상한값" (즉, 경로 상에서 r 값들의 bottleneck)을 계산합니다.

void dijkstra(const vector<vector<Edge>> &graph, vector<int> &dist, int min_size) {

    int n = graph.size() - 1;

    dist.assign(n + 1, 0);

    dist[1] = INF;

    // 기본 priority_queue는 큰 값부터 pop하므로 max-heap처럼 사용합니다.

    priority_queue<pair<int, int>> pq;

    pq.push({INF, 1});

    

    while (!pq.empty()) {

        auto [d, u] = pq.top();

        pq.pop();

        if (d < dist[u])

            continue;

        for (const auto &edge : graph[u]) {

            int v = edge.v, l = edge.l, r = edge.r;

            if (min_size < l || min_size > r)

                continue;

            int nd = min(r, d);

            if (nd > dist[v]) {

                dist[v] = nd;

                pq.push({nd, v});

            }

        }

    }

}

 

int main(){

    ios::sync_with_stdio(false);

    cin.tie(nullptr);

    

    int n, m;

    cin >> n >> m;

    vector<vector<Edge>> graph(n + 1);

    vector<int> min_list;

    

    for (int i = 0; i < m; i++){

        int u, v, l, r;

        cin >> u >> v >> l >> r;

        min_list.push_back(l);

        graph[u].push_back({v, l, r});

        graph[v].push_back({u, l, r});

    }

    sort(min_list.begin(), min_list.end());

    

    int k;

    cin >> k;

    vector<int> fish(k);

    for (int i = 0; i < k; i++){

        cin >> fish[i];

    }

    sort(fish.begin(), fish.end());

    

    int answer = 0;

    int idx = 0;

    int left_bound = 0, right_bound = 0;

    vector<int> dist(n + 1, 0);

    

    // 각 간선의 l 값을 순회하면서

    // 1번에서 n번까지 도달할 때 가능한 fish 크기의 범위를 구하고

    // 그 범위에 해당하는 fish를 two-pointer 방식으로 센다.

    for (int lower : min_list) {

        dijkstra(graph, dist, lower);

        if (dist[n] < lower)

            continue;

        left_bound = lower;

        right_bound = max(right_bound, dist[n]);

        while (true) {

            if (idx == k)

                break;

            if (fish[idx] < left_bound)

                idx++;

            else if (fish[idx] <= right_bound) {

                idx++;

                answer++;

            } else

                break;

        }

    }

    

    cout << answer << "\n";

    return 0;

}