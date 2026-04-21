#include <bits/stdc++.h>
using namespace std;

struct Query {
    int l, r, idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, c;
    cin >> n >> c;

    vector<int> arr(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> arr[i];
    }

    int m;
    cin >> m;

    vector<int> answer(m, 0);
    vector<Query> query(m);

    for (int idx = 0; idx < m; ++idx) {
        int i, j;
        cin >> i >> j;
        query[idx] = {i, j, idx};
    }

    int blk = (int)std::sqrt(n);

    sort(query.begin(), query.end(), [&](const Query &a, const Query &b) {
        int ab = a.l / blk;
        int bb = b.l / blk;
        if (ab != bb) return ab < bb;
        if (ab % 2 == 0) return a.r < b.r;
        else return a.r > b.r;
    });

    int left = 1, right = 0;

    // rnk[색깔] -> 순위, info[순위] -> 색깔
    vector<int> rnk(c + 1), info(c + 1), cnt(c + 1, 0);
    for (int i = 0; i <= c; ++i) {
        rnk[i] = i;
        info[i] = i;
    }

    for (const auto &q : query) {
        int i = q.l;
        int j = q.r;
        int idx = q.idx;

        while (right < j) {
            ++right;
            int color = arr[right];
            ++cnt[color];
            while (true) {
                if (rnk[color] == 1) break;
                int other_color = info[rnk[color] - 1];
                if (cnt[color] <= cnt[other_color]) break;
                // 순위 swap
                swap(info[rnk[color]], info[rnk[color] - 1]);
                rnk[other_color]++;
                rnk[color]--;
            }
        }

        while (right > j) {
            int color = arr[right];
            --cnt[color];
            while (true) {
                if (rnk[color] == c) break;
                int other_color = info[rnk[color] + 1];
                if (cnt[color] >= cnt[other_color]) break;
                swap(info[rnk[color]], info[rnk[color] + 1]);
                rnk[other_color]--;
                rnk[color]++;
            }
            --right;
        }

        while (left < i) {
            int color = arr[left];
            --cnt[color];
            while (true) {
                if (rnk[color] == c) break;
                int other_color = info[rnk[color] + 1];
                if (cnt[color] >= cnt[other_color]) break;
                swap(info[rnk[color]], info[rnk[color] + 1]);
                rnk[other_color]--;
                rnk[color]++;
            }
            ++left;
        }

        while (left > i) {
            --left;
            int color = arr[left];
            ++cnt[color];
            while (true) {
                if (rnk[color] == 1) break;
                int other_color = info[rnk[color] - 1];
                if (cnt[color] <= cnt[other_color]) break;
                swap(info[rnk[color]], info[rnk[color] - 1]);
                rnk[other_color]++;
                rnk[color]--;
            }
        }

        // 최빈 색이 과반인지 확인
        int bestColor = info[1];
        if (cnt[bestColor] * 2 > (j - i + 1)) {
            answer[idx] = bestColor;
        } else {
            answer[idx] = 0;
        }
    }

    for (int x : answer) {
        if (x == 0) {
            cout << "no\n";
        } else {
            cout << "yes " << x << "\n";
        }
    }

    return 0;
}
