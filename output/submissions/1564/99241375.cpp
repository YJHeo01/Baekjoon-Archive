#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>

#define INF 100000
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;

    cin >> n;

    int answer = 1;

    for (int i = 1;i <= n;i++) {
        answer *= i;
        while (answer) {
            if (answer % 10 != 0) break;
            answer /= 10;
        }
        answer %= INF;
    }

    for (int i = 4;i >= 0;i--) {
        if (answer < pow(10,i)) cout << 0;
    }
    cout << answer;

    return 0;
}
