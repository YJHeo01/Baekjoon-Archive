#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>

#define INF 987654321

using namespace std;

int arr[100001] = { 0, };
int idx[100001];
int answer[100000] = { 0, };

int blk = 0;
bool compare(vector<int>& a, vector<int>& b) {
    if (a[0] / blk != b[0] / blk) return a[0] < b[0];
    return a[1] < b[1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;

    cin >> n;

    fill(idx, idx + 100001, -1);

    for (int i = 1;i <= n;i++) {
        int tmp;
        cin >> tmp;
        arr[i] = tmp;
    }

    int m;

    cin >> m;

    vector<vector<int>> info;
    vector<vector<int>> query;

    for (int k = 0;k < m;k++) {
        int i, j;
        cin >> i >> j;
        query.push_back({ i,j,k });
    }

    blk = (int)sqrt(n);

    sort(query.begin(), query.end(), compare);

    int left = 1;
    int right = 0;

    for (auto q : query) {
        int i = q[0];
        int j = q[1];
        int k = q[2];
        set<int> s;
        while (right < j) {
            right++;
            s.insert(arr[right]);
            if (idx[arr[right]] == -1) {
                idx[arr[right]] = info.size();
                info.push_back({ arr[right],1});
            }
            else {
                info[idx[arr[right]]][1]++;
            }
        }
        while (right > j) {
            s.insert(arr[right]);
            info[idx[arr[right]]][1]--;
            right--;
        }
        while (left < i) {
            s.insert(arr[left]);
            info[idx[arr[left]]][1]--;
            left++;
        }
        while (left > i) {
            left--;
            s.insert(arr[left]);
            if (idx[arr[left]] == -1) {
                idx[arr[left]] = info.size();
                info.push_back({ arr[left],1});
            }
            else {
                info[idx[arr[left]]][1]++;
            }
        }
        for (int value : s) {
            int pos = idx[value];
            while (1) {
                if (pos == 0 or info[pos - 1] [1] >= info[pos][1]) break;
                swap(idx[info[pos][0]], idx[info[pos - 1][0]]);
                swap(info[pos], info[pos - 1]);
                pos--;
            }
            while (1) {
                if (pos == info.size()-1 or info[pos + 1][1] <= info[pos][1]) break;
                swap(idx[info[pos][0]], idx[info[pos + 1][0]]);
                swap(info[pos], info[pos + 1]);
                pos++;
            }
        }
        answer[k] = info[0][1];
    }

    for (int i = 0;i < m;i++) {
        cout << answer[i] << "\n";
    }

    return 0;
}