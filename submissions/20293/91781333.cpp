#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int pos[1002][2] = { 0, };
int charge[1002] = { 0 };
int fuel[1002] = { 0, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    cin >> r >> c;
    int n;
    cin >> n;

    // 총 노드 개수: 시작 (0) + 중간 n개 (1~n) + 도착 (n+1)
    int total = n + 2;
    pos[0][0] = 1;pos[0][1] = 1;


    // 중간 정류장 정보 읽기
    for (int i = 1; i <= n; i++) {
        int a, b, z;
        cin >> a >> b >> z;
        pos[i][0] = a;
        pos[i][1] = b;
        charge[i + 1] = z;
    }

    pos[n + 1][0] = r;
    pos[n + 1][1] = c;
    // 도착 위치 (r, c)

    // 각 노드간 연결 정보를 담은 그래프 생성
    vector<vector<int>> graph(total);
    for (int i = 0; i < total; i++) {
        for (int j = 0; j < total; j++) {
            if (i == j) continue;
            // 현재 노드 i에서 노드 j로 이동 가능한지 검사 (행, 열 모두 증가)
            if (pos[j][0] >= pos[i][0] && pos[j][1] >= pos[i][1])
                graph[i].push_back(j);
        }
    }

    int answer = r * c;
    int left = 0, right = r * c;
    fill(fuel, fuel + 1002, -1);
    // 이분 탐색을 통해 최소 초기 연료(mid) 값을 찾는다.
    while (left <= right) {
        int mid = (left + right) / 2;
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
                int nf = f + (pos[x][0] - pos[nx][0]) + (pos[x][1] - pos[nx][1]) + charge[x];
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
            fill(fuel, fuel + 1002, -1);
        }
        else {
            left = mid + 1;
        }
    }

    cout << answer << "\n";
    return 0;
}