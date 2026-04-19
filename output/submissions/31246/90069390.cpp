#include <iostream>
#include <algorithm>

using namespace std;

int cost[100000] = { 0, };

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    for (int i = 0;i < n;i++) {
        int a, b;
        cin >> a >> b;
        cost[i] = (b - a);
    }
    sort(cost, cost + n);
    int answer = cost[k - 1];
    if (answer < 0) answer = 0;
    cout << answer;
}