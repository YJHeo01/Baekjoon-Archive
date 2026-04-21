#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <map>

using namespace std;

int answer[1000001] = { 0, };

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	
	while (1) {
		int n;
		cin >> n;
		if (n == 0) break;
		if (n == 1 || answer[n] != 0) { cout << answer[n] << "\n"; continue; }
		int cnt = 1;
		int left = 1;int right = 1;
		int tmp = 2;

		while (left <= right) {
			if (left + right + 2 > n) break;
			if (tmp > n) {
				left++; tmp -= left;
			}
			else if (tmp < n) {
				right++; tmp += (right+1);
			}
			else {
				cnt++;
				left++; tmp -= left;
				right++; tmp += (right + 1);
			}
		}
		cout << cnt << "\n";
		answer[n] = cnt;
	}
}