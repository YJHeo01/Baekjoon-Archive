#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <map>

using namespace std;

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	
	while (1) {
		int n;
		cin >> n;
		if (n == 0) break;
		int answer = 0;
		int left = 1;int right = 1;
		int tmp = 2;
		while (left <= right) {
			if (tmp > n) {
				left++; tmp -= left;
			}
			else if (tmp < n) {
				right++; tmp += (right+1);
			}
			else {
				answer++;
				left++; tmp -= left;
				right++; tmp += (right + 1);
			}
		}
		cout << answer << "\n";
	}
}