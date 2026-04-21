#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
    }

    // 알파벳마다 고유 인덱스 매핑
    unordered_map<char,int> alphabet;
    int k = 0;
    for (auto &s : words) {
        for (char c : s) {
            if (alphabet.find(c) == alphabet.end()) {
                alphabet[c] = k++;
            }
        }
    }

    // 0,1,...,k-1 순열을 생성하기 위한 초기 벡터
    vector<int> perm(k);
    iota(perm.begin(), perm.end(), 0);

    ll answer = 0;
    // 모든 순열을 순회 (Python의 itertools.permutations 과 동일)
    do {
        ll value = 0;
        for (auto &s : words) {
            ll tmp = 0;
            for (char c : s) {
                int idx = alphabet[c];           // 알파벳 고유 인덱스
                int digit = 9 - perm[idx];      // 대응되는 숫자
                tmp = tmp * 10 + digit;
            }
            value += tmp;
        }
        answer = max(answer, value);
    } while (next_permutation(perm.begin(), perm.end()));

    cout << answer << "\n";
    return 0;
}
