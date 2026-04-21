#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <tuple>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    cin >> h >> w;
    
    vector<vector<int>> maze(h, vector<int>(w));
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            cin >> maze[i][j];
        }
    }
    
    // array 초기화: maze의 값이 0 이하이면 해당 값으로, 아니면 0으로 초기화
    vector<vector<int>> arr(h, vector<int>(w, 0));
    
    // 우선순위 큐에 (높이, x, y)를 저장 (높이가 큰 순으로 꺼내기 위해 custom comparator 사용)
    using T = tuple<int, int, int>;
    auto cmp = [](const T &a, const T &b) {
        return get<0>(a) < get<0>(b); // 더 큰 값이 우선
    };
    priority_queue<T, vector<T>, decltype(cmp)> pq(cmp);
    
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            if (maze[i][j] <= 0)
                arr[i][j] = maze[i][j];
            else
                pq.push(make_tuple(maze[i][j], i, j));
        }
    }
    
    int answer = 0;
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    
    while (!pq.empty()){
        int l, x, y;
        tie(l, x, y) = pq.top();
        pq.pop();
        
        if (arr[x][y] >= l) continue;
        
        arr[x][y] = l;
        deque<pair<int, int>> dq;
        dq.push_back({x, y});
        answer++;
        
        while (!dq.empty()){
            int vx = dq.front().first;
            int vy = dq.front().second;
            dq.pop_front();
            
            for (int i = 0; i < 4; i++){
                int nx = vx + dx[i];
                int ny = vy + dy[i];
                
                if (nx < 0 || ny < 0 || nx >= h || ny >= w) continue;
                if (maze[nx][ny] == -1) continue;
                if (arr[vx][vy] - 1 < maze[nx][ny]) continue;
                if (arr[nx][ny] >= arr[vx][vy] - 1) continue;
                
                arr[nx][ny] = arr[vx][vy] - 1;
                if (arr[nx][ny] > maze[nx][ny]){
                    cout << -1 << "\n";
                    return 0;
                }
                if (arr[nx][ny] != 1)
                    dq.push_back({nx, ny});
            }
        }
    }
    
    cout << answer << "\n";
    return 0;
}

/*
기존 제출 코드(결과 TLE)를 챗GPT로 변환
from collections import deque
import sys,heapq

input = sys.stdin.readline

h,w = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(h)]

q = []

array = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if maze[i][j] <= 0: array[i][j] = maze[i][j]
        else: heapq.heappush(q,(-maze[i][j],i,j))

answer = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while q:
    l,x,y = heapq.heappop(q)
    l *= -1
    if array[x][y] >= l: continue
    array[x][y] = l
    queue = deque([(x,y)])
    answer += 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
            if maze[nx][ny] == -1 or array[vx][vy] - 1 < maze[nx][ny] or array[nx][ny] >= array[vx][vy] - 1: continue
            array[nx][ny] = array[vx][vy] - 1
            if array[nx][ny] > maze[nx][ny]:
                print(-1)
                exit(0)
            if array[nx][ny] != 1: queue.append((nx,ny))
                

print(answer)

*/
