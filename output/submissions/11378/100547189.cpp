#include <iostream>

#include <vector>

#include <algorithm>

using namespace std;

bool visited[1001];

vector<int> adj[1001];

int A[1001];

vector<int> B(1001, -1);

bool dfs(int a) {

	visited[a] = true;	for (int b : adj[a]) {

		if (B[b] == -1 || (!visited[B[b]] && dfs(B[b]))) {

			A[a] = b;

			B[b] = a;

			return true;

		}

	}

	return false;

}

int main(void)

{

	ios_base::sync_with_stdio(false);

	cin.tie(NULL);

	cout.tie(NULL);

	int n, m, k;

	cin >> n >> m >> k;

	for (int i = 1;i <= n;i++) {

		int cnt;

		cin >> cnt;

		for (int j = 0;j < cnt;j++) {

			int tmp;

			cin >> tmp;

			adj[i].push_back(tmp);

		}

	}

	int answer = 0;

	fill(A, A + n + 1, -1);

for(int x=0;x<=k;x++){

	for (int i = 1;i <= n;i++) {
        if(A[i]==adj[i][adj[i].size()-1])continue;

		fill(visited, visited + n + 1, false);

		if (dfs(i))answer++;

	}
}

	cout << answer;

}