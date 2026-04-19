//chatgpt 테스트 용

#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
const int64 LIM = 100'000'000'001LL;      // 10^11 + 1 (MEGA 판정용)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, k;
    int64 s;
    if (!(cin >> N >> k >> s)) return 0;

    vector<int> A(N);
    for (int &x : A) cin >> x;

    int K = min(k, 37);                   // 실제로 관리할 최대 강화 횟수
    vector<int64> dp(K + 1, -1);          // -1 : 불가능
    if (s > 0) dp[0] = s;

    for (int ai : A) {
        vector<int64> nxt(K + 1, -1);
        for (int j = 0; j <= K; ++j) {
            if (dp[j] <= 0) continue;     // 이미 죽었음

            // 1) 먹이 주기
            int64 sz = dp[j] + ai;
            if (sz > 0) {
                nxt[j] = max(nxt[j], min(sz, LIM));
            }

            // 2) 강화
            if (j < K) {
                sz = dp[j] << 1;          // ×2
                if (sz > LIM) sz = LIM;
                nxt[j + 1] = max(nxt[j + 1], sz);
            }
        }
        dp.swap(nxt);
    }

    int64 best = *max_element(dp.begin(), dp.end());
    if (best <= 0) {
        cout << -1 << '\n';
    } else if (best > 100'000'000'000LL) {
        cout << "MEGA\n";
    } else {
        cout << best << '\n';
    }
    return 0;
}
