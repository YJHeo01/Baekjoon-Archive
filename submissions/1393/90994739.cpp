#include <iostream>
#include <cmath>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int xs, ys;
	cin >> xs >> ys;

	int xe, ye, dx, dy;

	cin >> xe >> ye >> dx >> dy;

	for (int i = 2;i <= 100;i++) {
		if (dx % i == 0 and dy % i == 0) {
			dx /= i;
			dy /= i;
		}
	}
	int answer_x = xe;
	int answer_y = ye;
	
	while (1) {
		xe += dx;
		ye += dy;
		if (pow((xe - xs), 2) + pow((ye - ys), 2) > pow((answer_x - xs), 2) + pow((answer_y - ys), 2)) break;
		answer_x = xe;
		answer_y = ye;
	}

	cout << answer_x << " " << answer_y;
}