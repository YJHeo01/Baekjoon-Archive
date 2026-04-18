#include <bits/stdc++.h>
using namespace std;

static const int INF = 200000;
static const int SHIFT = 100000;

inline void update(vector<int>& tree, int size, int pos, int value) {
    int i = size + pos;
    tree[i] += value;
    i >>= 1;
    while (i >= 1) {
        tree[i] = max(tree[i * 2], tree[i * 2 + 1]);
        i >>= 1;
    }
}

inline int query(const vector<int>& tree, int size, int l, int r) {
    l += size;
    r += size;
    int res = 0;
    while (l <= r) {
        if (l % 2 == 1) {
            res = max(res, tree[l]);
            l += 1;
        }
        if (r % 2 == 0) {
            res = max(res, tree[r]);
            r -= 1;
        }
        l >>= 1;
        r >>= 1;
    }
    return res;
}

struct Q {
    int i, j, idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int n, q;
        cin >> n;
        if (!cin) return 0;
        if (n == 0) break;
        cin >> q;

        vector<int> arr(n + 1);
        for (int i = 1; i <= n; i++) cin >> arr[i];

        for (int i = 1; i <= n; i++) {
            arr[i] += SHIFT;
        }

        vector<int> answer(q, 0);

        vector<Q> query_s;
        query_s.reserve(q);

        for (int idx = 0; idx < q; idx++) {
            int i, j;
            cin >> i >> j;
            query_s.push_back({i, j, idx});
        }

        int blk = (int)sqrt(n);

        sort(query_s.begin(), query_s.end(), [&](const Q& a, const Q& b) {
            int ab = a.i / blk;
            int bb = b.i / blk;
            if (ab != bb) return ab < bb;
            if ((ab & 1) == 0) return a.j < b.j;
            return a.j > b.j;
        });

        int left = 1, right = 0;

        // Python: s_length = 2 ** ceil(log2(200001)+1)
        // => size = power of 2 >= 200001
        int size = 1;
        while (size < (INF + 1)) size <<= 1;
        int s_length = size * 2;

        vector<int> s(s_length, 0);

        for (auto [i, j, idx] : query_s) {
            while (right < j) {
                right += 1;
                update(s, size, arr[right], 1);
            }
            while (right > j) {
                update(s, size, arr[right], -1);
                right -= 1;
            }
            while (left < i) {
                update(s, size, arr[left], -1);
                left += 1;
            }
            while (left > i) {
                left -= 1;
                update(s, size, arr[left], 1);
            }
            answer[idx] = query(s, size, 0, INF);
            // (여기서는 query(0, INF) == s[1] 이라 answer[idx] = s[1]; 로도 가능)
        }

        for (int k = 0; k < q; k++) {
            cout << answer[k] << "\n";
        }
    }

    return 0;
}
