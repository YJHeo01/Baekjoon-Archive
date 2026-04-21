#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);

	int N;

	cin >> N;

	vector<vector<vector<int>>> x_start(30001);
	bool x_end[30002] = { false, };
	fill(x_end, x_end + 30001, false);

	for (int i = 0;i < N;i++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		x_end[x2] = true;
		x_start[x1].push_back({ y1,y2,x2 });
	}

	int answer = 0;
	
	int tmp = 0;

	vector<vector<int>> area;

	for (int i = 0;i <= 30000;i++) {
		if (x_end[i] == false and x_start[i].empty()) { answer += tmp; continue; }
		tmp = 0;
		if (!x_start[i].empty()) {
			for (vector<int> a : x_start[i]) {
				area.push_back(a);
			}
		}
		if (x_end[i]) {
			for (int j = 0;j < area.size();j++) {
				if (area[j][2] <= i) area[j][0] = 100000;
			}
		}
		sort(area.begin(), area.end());
		while (!area.empty()) {
			if (area.back()[0] < 100000) break;
			area.pop_back();
		}
		int left = 0;
		int right = 0;
		for (int j = 0;j < area.size();j++) {
			int new_left = area[j][0];
			int new_right = area[j][1];
			if (new_left > right) {
				tmp += (right - left);
				left = new_left;
			}
			right = max(new_right, right);
		}
		tmp += (right - left);
		answer += tmp;
	}

	cout << answer;

	return 0;
}