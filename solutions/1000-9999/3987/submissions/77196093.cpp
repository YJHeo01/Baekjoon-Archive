#define INF 100000000

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int n, m;
char space[500][500] = { 0, };
int visited[4][500][500] = { 0, };
bool meet_blackhole(char value);
bool escape_planetary_system(int x, int y);
bool loop(int x, int y, int d);
char get_direction_type(int value);
int get_new_direction(char planet_type, int cur_direction);
int dfs(char space[][500], int visited[][500][500], int x, int y, int d);

int main() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%s", space[i]);
	}
	int pr, pc;
	scanf("%d %d", &pr, &pc);
	int answer_direction = 0;
	int answer_time = 0;
	pr -= 1; pc -= 1;
	for (int direction = 0; direction < 4; direction++) {
		visited[direction][pr][pc] = 1;
		int tmp = dfs(space, visited, pr, pc, direction);
		if (tmp > answer_time) {
			answer_time = tmp;
			answer_direction = direction;
		}
		visited[direction][pr][pc] = 0;
	}
	if (space[pr][pc] == 'C') {
		answer_time = 0;
	}
	printf("%c\n", get_direction_type(answer_direction));
	if (answer_time >= INF) {
		printf("Voyager");
	}
	else {
		printf("%d", answer_time);
	}
}

int dfs(char space[][500], int visited[][500][500], int vx, int vy, int vd) {
	int dx[4] = { -1,0,1,0 };
	int dy[4] = { 0,1,0,-1 };
	int nx = vx; int ny = vy; int nd = vd;
	nd = get_new_direction(space[vx][vy], vd);
	nx += dx[nd];
	ny += dy[nd];
	if (escape_planetary_system(nx, ny) == true || meet_blackhole(space[nx][ny]) == true) {
		return visited[vd][vx][vy];
	}
	if (loop(nx, ny, nd) == true) {
		return INF;
	}
	visited[nd][nx][ny] = visited[vd][vx][vy] + 1;
	int ret_value = dfs(space, visited, nx, ny, nd);
	visited[nd][nx][ny] = 0;
	return ret_value;
}


bool escape_planetary_system(int x, int y) {
	if (x < 0 || y < 0 || x >= n || y >= m) {
		return true;
	}
	return false;
}

bool meet_blackhole(char value) {
	if (value == 'C') {
		return true;
	}
	return false;
}

int get_new_direction(char planet_type, int cur_direction) {
	if (planet_type == '.') {
		return cur_direction;
	}
	else if (planet_type == '/') {
		switch (cur_direction)
		{
		case 0:
			return 1;
		case 1:
			return 0;
		case 2:
			return 3;
		default:
			return 2;
		}
	}
	else {
		switch (cur_direction)
		{
		case 0:
			return 3;
		case 3:
			return 0;
		case 2:
			return 1;
		default:
			return 2;
			break;
		}
	}
}

bool loop(int x, int y, int d) {
	if (visited[d][x][y] != 0) {
		return true;
	}
	return false;
}

char get_direction_type(int value) {
	char direction_type[4] = { 'U','R','D','L' };
	return direction_type[value];
}