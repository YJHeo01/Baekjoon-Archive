#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int cal();

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int today = cal();
    int n;
    cin >> n;

    int answer = 0;

    for (int i = 0;i < n;i++) {
        int tmp = cal();
        if (tmp >= today) answer++;
    }

    cout << answer;
}

int cal() {
    int ret_value = 0;

    string today;

    cin >> today;

    for (char i:today) {
        if (i == '-') continue;
        ret_value *= 10;
        ret_value += i - '0';
    }

    return ret_value;
}