/*
    기존 제출한 소스코드를 생성형 AI로 변환
    https://www.acmicpc.net/source/95098256
*/


#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXV = 100000; // maximum value in arr

struct Query {
    int l, r, idx;
};

vector<int> tree;

// Segment tree: update position `pos` by `val` (+1 or -1)
void update(int node, int start, int end, int pos, int val) {
    if (pos < start || pos > end) return;
    if (start == end) {
        tree[node] += val;
        return;
    }
    int mid = (start + end) >> 1;
    if (pos <= mid) {
        update(node * 2, start, mid, pos, val);
    } else {
        update(node * 2 + 1, mid + 1, end, pos, val);
    }
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

// Segment tree: query sum in range [l, r]
int query(int node, int start, int end, int l, int r) {
    if (r < start || end < l) return 0;
    if (l <= start && end <= r) return tree[node];
    int mid = (start + end) >> 1;
    return query(node * 2, start, mid, l, r)
         + query(node * 2 + 1, mid + 1, end, l, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    vector<int> arr(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    int m;
    cin >> m;

    vector<Query> queries(m);
    for (int i = 0; i < m; i++) {
        cin >> queries[i].l >> queries[i].r;
        queries[i].idx = i;
    }

    // Block size for Mo's ordering
    int block = static_cast<int>(sqrt(n));

    // Sort queries in Mo's order (with alternating R order per block)
    sort(queries.begin(), queries.end(), [&](const Query &a, const Query &b) {
        int ablock = a.l / block;
        int bblock = b.l / block;
        if (ablock != bblock) {
            return ablock < bblock;
        }
        if ((ablock & 1) == 0) {
            return a.r < b.r;
        } else {
            return a.r > b.r;
        }
    });

    // Prepare segment tree of size 4 * (MAXV+1)
    tree.assign(4 * (MAXV + 1), 0);

    vector<ll> answer(m);
    ll currentAns = 0;
    int currL = 1, currR = 0;

    // Process each query
    for (auto &q : queries) {
        int L = q.l;
        int R = q.r;

        // Extend `currR` to the right
        while (currR < R) {
            currR++;
            int x = arr[currR];
            int leftVal = x - k;
            int rightVal = x + k;
            // Count how many in [leftVal, rightVal]
            currentAns += query(1, 0, MAXV, leftVal, rightVal);
            // Insert x into the tree
            update(1, 0, MAXV, x, +1);
        }

        // Shrink `currR` from the right
        while (currR > R) {
            int x = arr[currR];
            // Remove x from the tree
            update(1, 0, MAXV, x, -1);
            int leftVal = x - k;
            int rightVal = x + k;
            // Subtract its contributions
            currentAns -= query(1, 0, MAXV, leftVal, rightVal);
            currR--;
        }

        // Move `currL` to the right
        while (currL < L) {
            int x = arr[currL];
            // Remove x from the tree
            update(1, 0, MAXV, x, -1);
            int leftVal = x - k;
            int rightVal = x + k;
            currentAns -= query(1, 0, MAXV, leftVal, rightVal);
            currL++;
        }

        // Move `currL` to the left
        while (currL > L) {
            currL--;
            int x = arr[currL];
            int leftVal = x - k;
            int rightVal = x + k;
            currentAns += query(1, 0, MAXV, leftVal, rightVal);
            update(1, 0, MAXV, x, +1);
        }

        answer[q.idx] = currentAns;
    }

    // Output answers in original order
    for (int i = 0; i < m; i++) {
        cout << answer[i] << "\n";
    }

    return 0;
}
