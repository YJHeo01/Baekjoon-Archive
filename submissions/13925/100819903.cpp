//https://www.acmicpc.net/source/90492024 과거에 제출한 python 코드를 AI를 이용해서 c++로 변환

#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 1000000007LL;

int n;
vector<ll> a;
int tree_size;
vector<ll> tree;

// (order, command_type, value)
// order: 명령이 들어온 순서 (0 ~ m-1)
// command_type: 1 = 더하기, 2 = 곱하기, 3 = 대입
using Command = tuple<int,int,ll>;

// 각 노드마다 min-heap (priority_queue with greater) 로 lazy 연산 저장
using PQ = priority_queue<Command, vector<Command>, greater<Command>>;
vector<PQ> lazy;

// 트리 초기화: 리프에 값 채우고 위로 올라가며 합 계산
void build() {
    // 리프 채우기
    for (int i = 0; i < n; i++) {
        tree[tree_size + i] += a[i];
        tree[tree_size + i] %= MOD;
    }
    // 내부 노드 채우기
    for (int i = tree_size - 1; i >= 1; i--) {
        tree[i] = (tree[i * 2] + tree[i * 2 + 1]) % MOD;
    }
}

// lazy[node] 에 쌓인 연산들을 실제 tree[node] 에 적용하고, 자식에게 전파
void update_lazy(int node, int start, int end) {
    auto &pq = lazy[node];
    while (!pq.empty()) {
        auto [order, c, v] = pq.top();
        pq.pop();

        if (c == 1) {              // 덧셈
            tree[node] = (tree[node] + v) % MOD;
        } else if (c == 2) {       // 곱셈
            tree[node] = (tree[node] * (v % MOD)) % MOD;
        } else {                   // 대입: 구간 전체를 v로
            ll len = (ll)(end - start + 1);
            tree[node] = ((v % MOD) * (len % MOD)) % MOD;
        }

        // 리프가 아니면 자식에게도 같은 연산을 lazy 로 내려줌
        if (start != end) {
            lazy[node * 2].push({order, c, v});
            lazy[node * 2 + 1].push({order, c, v});
        }
    }
}

// 구간 [left, right] 에 command 연산 적용
void update(int node, int left, int right, int start, int end, const Command &command) {
    if (!lazy[node].empty()) {
        update_lazy(node, start, end);
    }

    if (start > right || end < left) return;  // 겹치지 않음

    if (left <= start && end <= right) {      // 완전히 포함
        lazy[node].push(command);
        update_lazy(node, start, end);
        return;
    }

    int mid = (start + end) / 2;
    update(node * 2, left, right, start, mid, command);
    update(node * 2 + 1, left, right, mid + 1, end, command);
    tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD;
}

// 구간 [left, right] 합 쿼리
ll query(int node, int left, int right, int start, int end) {
    if (!lazy[node].empty()) {
        update_lazy(node, start, end);
    }

    if (start > right || end < left) return 0;   // 겹치지 않음
    if (left <= start && end <= right) return tree[node];

    int mid = (start + end) / 2;
    ll lsum = query(node * 2, left, right, start, mid);
    ll rsum = query(node * 2 + 1, left, right, mid + 1, end);
    return (lsum + rsum) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    a.assign(n, 0);
    for (int i = 0; i < n; i++) cin >> a[i];

    // tree_size = 2^ceil(log2(n))
    tree_size = 1;
    while (tree_size < n) tree_size <<= 1;

    tree.assign(2 * tree_size, 0);
    lazy.assign(2 * tree_size, PQ());

    build();

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int t;
        cin >> t;
        if (t == 4) {
            int x, y;
            cin >> x >> y;
            // 입력은 1-indexed, 내부는 0-indexed
            cout << query(1, x - 1, y - 1, 0, n - 1) % MOD << '\n';
        } else {
            int x, y;
            ll v;
            cin >> x >> y >> v;
            Command cmd = {i, t, v};
            update(1, x - 1, y - 1, 0, n - 1, cmd);
        }
    }

    return 0;
}
