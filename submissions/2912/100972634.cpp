#include <bits/stdc++.h>
using namespace std;

void update(vector<int> &tree, int size, int pos, int value) {
    int i = size + pos;
    tree[i] += value;
    i /= 2;
    while (i >= 1) {
        tree[i] = tree[i * 2] + tree[i * 2 + 1];
        i /= 2;
    }
}

int query(const vector<int> &tree, int size, int l, int r) {
    l += size;
    r += size;
    int res = 0;
    while (l <= r) {
        if (l % 2 == 1) {
            res += tree[l];
            l++;
        }
        if (r % 2 == 0) {
            res += tree[r];
            r--;
        }
        l /= 2;
        r /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, c;
    cin >> n >> c;

    vector<int> arr(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    // size: 세그트리 리프 시작 인덱스 (2의 거듭제곱)
    int size = 1;
    while (size < n) size <<= 1;
    int s_length = size * 2;  // 전체 트리 배열 크기 (최대 인덱스 = 2*size)

    // 각 색깔별 등장 위치 저장
    vector<vector<int>> pos(c + 1);
    for (int i = 1; i <= n; i++) {
        pos[arr[i]].push_back(i);
    }

    int m;
    cin >> m;

    vector<int> answer(m, 0);
    vector<tuple<int,int,int>> querys;
    querys.reserve(m);

    for (int idx = 0; idx < m; idx++) {
        int i, j;
        cin >> i >> j;
        querys.emplace_back(i, j, idx);
    }

    // 색깔 하나씩 세그트리로 처리
    for (int color = 1; color <= c; color++) {
        if (pos[color].empty()) continue;

        // 매 색깔마다 새로운 세그트리 생성
        vector<int> s(s_length + 1, 0);

        // 해당 색깔이 등장하는 위치들을 1로 세팅
        for (int p : pos[color]) {
            update(s, size, p, 1);
        }

        // 모든 쿼리에 대해 이 색깔이 다수인지 확인
        for (auto &q : querys) {
            int i, j, idx;
            tie(i, j, idx) = q;
            if (answer[idx] != 0) continue;  // 이미 다수 색깔이 정해진 쿼리

            int cnt = query(s, size, i, j);
            if (cnt * 2 > (j - i + 1)) {
                answer[idx] = color;
            }
        }
    }

    for (int i = 0; i < m; i++) {
        if (answer[i] == 0) {
            cout << "no\n";
        } else {
            cout << "yes " << answer[i] << "\n";
        }
    }

    return 0;
}