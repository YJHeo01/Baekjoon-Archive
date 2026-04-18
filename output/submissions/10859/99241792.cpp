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
    
    int prime = 1;

    for (int i = 2;i <= (int)sqrt(n);i++) {
        if (n % i == 0) prime = 0;
    }

    int new_value = 0;

    for (int i = 1;i <= 8;i++) {
        int base = pow(10, i);
        if (base > n * 10) break;
        int tmp = n % base;
        for (int j = 0;j < i - 1;j++) {
            tmp /= 10;
        }
        tmp %= 10;
        if (tmp == 6) tmp = 9;
        else if (tmp == 9) tmp = 6;
        else if (tmp == 3 || tmp == 4 || tmp == 7) prime = 0;
        new_value *= 10;
        new_value += tmp;
    }

    for (int i = 2;i <= (int)sqrt(new_value);i++) {
        if (new_value % i == 0) prime = 0;
    }

    if (prime) cout << "yes";
    else cout << "no";

    return 0;
}