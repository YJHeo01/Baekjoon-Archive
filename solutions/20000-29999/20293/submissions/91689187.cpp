//직전 python 제출 코드(직접 작성) c++로 변환 (GPT 이용)

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    cin >> r >> c;
    int n;
    cin >> n;

    // 총 노드 개수: 시작 (0) + 중간 n개 (1~n) + 도착 (n+1)
    int total = n + 2;
    vector<int> charge(total, 0);
    vector<pair<int, int>> pos;

    // 시작 위치 (1, 1)
    pos.push_back({ 1,1 });

    // 중간 정류장 정보 읽기
    for (int i = 0; i < n; i++) {
        int a, b, z;
        cin >> a >> b >> z;
        pos.push_back({ a, b });
        charge[i + 1] = z;
    }

    // 도착 위치 (r, c)
    pos.push_back({ r, c });

    // 각 노드간 연결 정보를 담은 그래프 생성
    vector<vector<int>> graph(total);
    for (int i = 0; i < total; i++) {
        for (int j = 0; j < total; j++) {
            if (i == j) continue;
            // 현재 노드 i에서 노드 j로 이동 가능한지 검사 (행, 열 모두 증가)
            if (pos[j].first >= pos[i].first && pos[j].second >= pos[i].second)
                graph[i].push_back(j);
        }
    }

    int answer = r * c;
    int left = 0, right = r * c;

    // 이분 탐색을 통해 최소 초기 연료(mid) 값을 찾는다.
    while (left <= right) {
        int mid = (left + right) / 2;
        vector<int> fuel(total, -1);
        fuel[0] = mid;

        // 우선순위 큐를 사용하여 현재 연료(fuel) 값이 큰 노드부터 탐색
        // 기본 priority_queue는 최대 힙(max-heap)이다.
        priority_queue<pair<int, int>> pq;
        pq.push({ mid, 0 });

        while (!pq.empty()) {
            auto [f, x] = pq.top();
            pq.pop();
            if (fuel[x] > f) continue;
            for (int nx : graph[x]) {
                // 이동 시 연료 계산:
                // nf = 현재 연료 - (거리 비용) + charge[x]
                int nf = f + (pos[x].first - pos[nx].first)
                    + (pos[x].second - pos[nx].second)
                    + charge[x];
                if (nf > fuel[nx]) {
                    fuel[nx] = nf;
                    pq.push({ nf, nx });
                }
            }
        }

        // 도착 노드(total-1)가 도달 가능한 경우
        if (fuel[total - 1] != -1) {
            answer = mid;
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }

    cout << answer << "\n";
    return 0;
}