from collections import deque
import sys

def bfs(board, start_r, start_c):
    # board_state는 tuple(tuple(...)) 형태로 저장하여 hashable하게 만든다.
    init_board = tuple(tuple(row) for row in board)
    # 상태: (현재 행, 현재 열, 이동 횟수, 먹은 사과 개수, 현재 board_state)
    queue = deque()
    queue.append((start_r, start_c, 0, 0, init_board))
    # 방문 기록에는 (행, 열, 이동 횟수, 먹은 사과 개수, board_state)를 포함
    visited = set()
    visited.add((start_r, start_c, 0, 0, init_board))
    
    while queue:
        r, c, moves, apples, board_state = queue.popleft()
        # 조건: 3번 이하 이동으로 사과를 2개 이상 먹은 경우
        if apples >= 2 and moves <= 3:
            return 1
        # 이동 횟수가 이미 3이면 더 이상 이동할 수 없음
        if moves == 3:
            continue
        
        # 상, 하, 좌, 우 이동
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                # 장애물이 있는 칸은 이동할 수 없음
                if board_state[nr][nc] == -1:
                    continue
                new_apples = apples
                # 현재 board_state를 리스트의 리스트로 복사
                new_board = [list(row) for row in board_state]
                # 학생이 현재 칸을 떠나면 장애물로 변경
                new_board[r][c] = -1
                # 만약 이동할 칸에 사과가 있다면, 사과를 먹고 해당 칸은 빈 칸으로 변경
                if new_board[nr][nc] == 1:
                    new_apples += 1
                    new_board[nr][nc] = 0
                # 새 board_state를 tuple로 변환
                new_board_state = tuple(tuple(row) for row in new_board)
                new_state = (nr, nc, moves + 1, new_apples, new_board_state)
                # 방문한 상태 키에 apple 정보도 포함 (보드 상태만 같아도 먹은 사과 개수는 다를 수 있음)
                state_key = (nr, nc, moves + 1, new_apples, new_board_state)
                if state_key not in visited:
                    visited.add(state_key)
                    queue.append(new_state)
    return 0

def main():
    input = sys.stdin.readline
    # 첫 줄: 학생의 시작 위치 (r, c)
    
    board = []
    # 이후 5줄: 5x5 보드 정보 (정수: 1=사과, -1=장애물, 0=빈 칸)
    for _ in range(5):
        board.append(list(map(int, input().split())))
    start_r, start_c = map(int, input().split())
    print(bfs(board, start_r, start_c))

if __name__ == '__main__':
    main()
