#include <iostream>

using namespace std;

int mask,n;
bool visited[24] = { 0, };

int backtracking(int x) {
	if (mask == x) return backtracking(x - 1);
	if (x == 0) return 1;
	int ret_value = 0;
	for (int nx = x+1;nx < 2 * n;nx++) {
		if (visited[nx] or visited[nx - x-1]) continue;
		visited[nx] = true;
		visited[nx - x - 1] = true;
		ret_value += backtracking(x - 1);
		visited[nx] = false;
		visited[nx - x - 1] = false;
	}
	return ret_value;
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int x, y;
	cin >> n >> x >> y;
	mask = y - x;
	if (mask == 1) {
		cout << 0;
		return 0;
	}
	mask--;
	fill(visited, visited + 24, false);
	visited[x - 1] = true;
	visited[y - 1] = true;
	int answer = backtracking(n);
	cout << answer;
}