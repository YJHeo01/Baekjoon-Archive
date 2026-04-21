#include <iostream>
#include <algorithm>

using namespace std;

long long int a[200000] = { 0, };
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long int answer = 0;
    long long int n, k;
    cin >> n >> k;
    for (int i = 0;i < n;i++) cin >> a[i];
    long long int tmp = 0;
    for (int i = 0;i < n;i++) {
        answer = max(answer, tmp + (k - i) * a[i]);
        tmp += a[i];
    }
    tmp = 0;
    for (int i = 0;i < n;i++) {
        answer = max(answer, tmp + (k - i) * a[n - 1 - i]);
        tmp += a[n - 1 - i];
    }
    cout << answer;
}