#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

void bfs(const vector<int>& grow, vector<vector<long long>>& size, int n, int k, long long s) {
    deque<pair<int, int>> queue;
    queue.push_back({0, 0});
    size[0][0] = s;

    while (!queue.empty()) {
        auto [day, cnt] = queue.front();
        queue.pop_front();
        if (day == n) continue;

        if (size[day][cnt] + grow[day] > size[day + 1][cnt]) {
            size[day + 1][cnt] = size[day][cnt] + grow[day];
            queue.push_back({day + 1, cnt});
        }
        if (cnt == k) continue;

        if (size[day][cnt] * 2 > size[day + 1][cnt + 1]) {
            size[day + 1][cnt + 1] = 2 * size[day][cnt];
            queue.push_back({day + 1, cnt + 1});
        }
    }
}

int main() {
    int n, k;
    long long s;
    cin >> n >> k >> s;

    if (k > 36) {
        cout << "MEGA" << endl;
        return 0;
    }

    vector<vector<long long>> size(n + 1, vector<long long>(k + 1, 0));
    vector<int> grow(n);
    for (int i = 0; i < n; ++i) {
        cin >> grow[i];
    }

    bfs(grow, size, n, k, s);
    long long answer = *max_element(size[n].begin(), size[n].end());

    if (answer > 100000000000LL) {
        cout << "MEGA" << endl;
    } else if (answer <= 0) {
        cout << -1 << endl;
    } else {
        cout << answer << endl;
    }

    return 0;
}