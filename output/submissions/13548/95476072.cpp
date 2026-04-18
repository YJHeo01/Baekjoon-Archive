#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>

#define INF 987654321

using namespace std;

int arr[100001] = { 0, };
int cnt_info[100001] = { 0, };
int num_cnt[100001] = { 0, };
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

    for (int i = 1;i <= n;i++) {
        int tmp;
        cin >> tmp;
        arr[i] = tmp;
    }

    int m;

    cin >> m;

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
    int max_cnt = 0;

    for (auto q : query) {
        int i = q[0];
        int j = q[1];
        int k = q[2];
        while (right < j) {
            right++;
            cnt_info[num_cnt[arr[right]]]--;
            num_cnt[arr[right]]++;
            cnt_info[num_cnt[arr[right]]]++;
            if (num_cnt[arr[right]] > max_cnt) max_cnt = num_cnt[arr[right]];
        }
        while (right > j) {
            cnt_info[num_cnt[arr[right]]]--;
            if (cnt_info[max_cnt] == 0) max_cnt--;
            right--;
        }
        while (left < i) {
            cnt_info[num_cnt[arr[left]]]--;
            if (cnt_info[max_cnt] == 0) max_cnt--;
            left++;
        }
        while (left > i) {
            left--;
            cnt_info[num_cnt[arr[left]]]--;
            num_cnt[arr[left]]++;
            cnt_info[num_cnt[arr[left]]]++;
            if (num_cnt[arr[left]] > max_cnt) max_cnt = num_cnt[arr[left]];
            
        }
        answer[k] = max_cnt;
    }

    for (int i = 0;i < m;i++) {
        cout << answer[i] << "\n";
    }

    return 0;
}