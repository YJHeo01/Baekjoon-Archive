#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>

#define INF 987654321

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    while (1) {
        long long int y, c, r;
        cin >> y >> c >> r;
        if (y == 0 and c == 0 and r == 0) break;
        long long int answer = y * c;
        long long int left = 0;
        long long int right = answer;
        while (left <= right) {
            long long int mid = (left + right) / 2;
            long long int money = mid;
            for (int i = 0;i < y;i++) {
                money -= c;
                if (money < 0) break;
                money += money * r / 100;
            }
            if (money >= 0) {
                answer = mid;
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        cout << answer << "\n";
    }

    return 0;
}