#define INF 987654321

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int arr[10000] = { 0, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    
    for (int i = 0;i < 2 * n;i++) {
        cin >> arr[i];
    }

    sort(arr, arr + 2 * n);

    int answer = arr[0] + arr[2 * n - 1];

    for (int i = 1;i < n;i++) {
        answer = min(answer, arr[i] + arr[2 * n - 1 - i]);
    }

    cout << answer;

    return 0;
}
